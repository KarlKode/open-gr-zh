import logging
import os
import re
from datetime import datetime

import aiofiles
import aiohttp
from fastapi import BackgroundTasks
from tortoise.functions import Max

from app.models import Meeting, AgendaItem, CouncilMember, Speech

log = logging.getLogger(__name__)

BASE_URL = "https://audio.gemeinderat-zuerich.ch/"
SPEECH_DL_DIR = "speech_audio"
CHUNK_SIZE = 4096

TOC_RE = r"^tocTab\[ir\+\+\] = new Array \(\"(?P<id>Top|\d+(?:\.\d+)*)\", \"(Navigation|(?P<item_announcements>Mitteilungen)|(?:(?P<item_id>(?P<item_year>\d{4})\/(?P<item_number>\d+)) (?P<item_title>.+?))|(?:Sitzung (?P<meet_nr>\d+) vom (?P<meet_date>\d{2}\.\d{2}\.\d{4}))|(?:(?:(?P<speaker_salutation>Frau|Herr|(?:(?:Stadtp|Ratsp|P)räsident(?:in)?)) )?(?P<speaker_name>\D+?) \((?P<speaker_party>[^\)]+)\))|(?P<item_misc>.+?))\", (?:tocLink|\"(?P<url>content\/[^\"]+)\")\); \/\/(?:(?P<updated_at>\d{4}\.\d{2}\.\d{2} \d{2}:\d{2}:\d{2}:\d+)|.*)$"
TOC_EXP = re.compile(TOC_RE, re.MULTILINE)


async def sync_meetings() -> None:
    log.debug("Syncing ZH meetings")
    async with aiohttp.ClientSession() as session:
        url = BASE_URL + "script/tocTab.js"
        log.debug("Fetching ZH meeting TOC from %s", url)
        async with session.get(url) as r:
            log.debug("Fetched ZH meeting TOC: %d (%r)", r.status, r.reason)
            try:
                r.raise_for_status()  # FIXME: handle non OK responses gracefully
            except aiohttp.ClientResponseError:
                log.warning(
                    "Failed to fetch ZH meeting TOC from %s", url, exc_info=True
                )
                raise
            t = await r.text()
            log.info("Fetched ZH meeting TOC from %s: %d bytes", url, len(t))

            entries = TOC_EXP.finditer(t)
            # assert len(list(entries)) == t.split("\n")[2:-1]  # Ignore first two lines (JS) and last line (newline).
            await sync_meetings_db(entries)


async def sync_speeches(background_tasks: BackgroundTasks) -> None:
    log.debug("Syncing ZH speeches")
    speeches_missing = (
        Speech.filter(mp3_path__isnull=True)
        .prefetch_related("item", "item__meeting")
        .order_by("item__meeting__id", "item__id")
    )
    async for speech in speeches_missing:
        background_tasks.add_task(sync_speech, speech)


async def sync_speech(speech: Speech) -> None:
    log.debug("Syncing ZH speech %s", speech)
    mp3_name = f"m{speech.item.meeting.id}_i{speech.item.id}_s{speech.id}.mp3"
    speech.mp3_path = os.path.join(SPEECH_DL_DIR, mp3_name)
    if not os.path.isfile(speech.mp3_path):
        await download_speech(speech)
    await speech.save()


async def sync_meetings_db(entries) -> None:
    meeting = None
    item_stack = []
    for m in entries:
        id_str = m.group("id")
        log.info("Handling entry %s: %r", id_str, m.groups())
        if id_str.find(".") == -1:
            if id_str == "Top":
                continue
            elif id_str[:2] == "20":
                break
            meeting_date = datetime.strptime(m.group("meet_date"), "%d.%m.%Y").date()
            meeting = await upsert_meeting(meeting_date, int(m.group("meet_nr")))
        else:
            parent = None
            while item_stack:
                item_id, item = item_stack[-1]
                if item_id in id_str:
                    parent = item
                    break
                item_stack.pop(-1)

            if (
                m.group("item_announcements")
                or m.group("item_id")
                or m.group("item_misc")
            ):
                title = None
                for group in ("item_announcements", "item_id", "item_misc"):
                    if m.group(group):
                        title = group
                        break
                if not title:
                    raise ValueError(
                        f"unexpected match: missing item title ({m.groups()!r})"
                    )
                item = await upsert_agenda_item(
                    m.group("item_id"), title, meeting, parent
                )
                item_stack.append((id_str, item))
            elif m.group("speaker_name"):
                if not item_stack:
                    raise ValueError(
                        f"invalid speech: empty item stack ({m.groups()!r})"
                    )
                _, item = item_stack[-1]

                member = await upsert_council_member(
                    m.group("speaker_name"), m.group("speaker_party")
                )
                await upsert_speech(member, item, m.group("url"))


async def upsert_council_member(name: str, party: str) -> CouncilMember:
    log.debug("Upsert Council Member: %s (%s)", name, party)
    cm = await CouncilMember.filter(name=name, party=party).first()
    if not cm:
        cm = await CouncilMember.create(name=name, party=party)
    return cm


async def upsert_meeting(date: datetime.date, meeting_number: int) -> Meeting:
    log.debug("Upserting meeting %s/%d", date.strftime("%d.%m.%Y"), meeting_number)
    m = await Meeting.filter(date=date, number=meeting_number).first()
    if not m:
        m = await Meeting.create(date=date, number=meeting_number)
    return m


async def upsert_agenda_item(
    gr_number: str | None,
    title: str,
    meeting: Meeting,
    parent: AgendaItem | None = None,
) -> AgendaItem:
    log.debug("Upserting agenda item %s: %s (%s)", gr_number, title, meeting)
    i = await AgendaItem.filter(
        gr_number=gr_number, meeting_id=meeting.id, title=title
    ).first()
    if not i:
        max_meeting_ordering = (
            await AgendaItem.filter(meeting_id=meeting.id)
            .annotate(max=Max("meeting_ordering"))
            .first()
            .values("max")
        )
        meeting_ordering = (
            max_meeting_ordering["max"] + 1
            if max_meeting_ordering and max_meeting_ordering["max"]
            else 1
        )
        i = await AgendaItem.create(
            gr_number=gr_number,
            title=title,
            meeting_id=meeting.id,
            meeting_ordering=meeting_ordering,
            parent_id=parent.id if parent else None,
        )
    return i


async def upsert_speech(member: CouncilMember, item: AgendaItem, url: str) -> Speech:
    log.debug("Upserting ZH speech: %s on %s: %s", member, item, url)
    s = await Speech.filter(council_member_id=member.id, item_id=item.id).first()
    if not s:
        max_item_ordering = (
            await Speech.filter(item_id=item.id)
            .annotate(max=Max("item_ordering"))
            .first()
            .values("max")
        )
        item_ordering = (
            max_item_ordering["max"] + 1
            if max_item_ordering and max_item_ordering["max"]
            else 1
        )
        mp3_file = (
            url.replace("content", "audio")
            .replace("_", " ")
            .replace(".html#Audio-PC ", "_")
            .replace("Audio-PC ", "")
            + ".mp3"
        )
        mp3_url = BASE_URL + mp3_file
        s = await Speech.create(
            council_member_id=member.id,
            item_id=item.id,
            item_ordering=item_ordering,
            mp3_url=mp3_url,
        )
    return s


async def download_speech(speech: Speech) -> None:
    async with aiohttp.ClientSession() as session:
        async with session.get(speech.mp3_url) as resp:
            # with open(speech.mp3_path, "wb") as fd:
            async with aiofiles.open(speech.mp3_path, "wb") as f:
                async for chunk in resp.content.iter_chunked(CHUNK_SIZE):
                    # fd.write(chunk)
                    await f.write(chunk)
