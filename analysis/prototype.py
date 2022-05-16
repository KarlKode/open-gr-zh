import os
import re
import shutil
from dataclasses import dataclass
from datetime import date, datetime
from typing import Any, Union

import requests

BASE_URL = "https://audio.gemeinderat-zuerich.ch/"

TOC_RE = r"^tocTab\[ir\+\+\] = new Array \(\"(?P<id>Top|\d+(?:\.\d+)*)\", \"(Navigation|(?P<item_announcements>Mitteilungen)|(?:(?P<item_id>(?P<item_year>\d{4})\/(?P<item_number>\d+)) (?P<item_title>.+?))|(?:Sitzung (?P<meet_nr>\d+) vom (?P<meet_date>\d{2}\.\d{2}\.\d{4}))|(?:(?:(?P<speaker_salutation>Frau|Herr|(?:(?:Rats|P)räsident(?:in)?)) )?(?P<speaker_name>\D+?) \((?P<speaker_party>[^\)]+)\))|(?P<item_misc>.+?))\", (?:tocLink|\"(?P<url>content\/[^\"]+)\")\); \/\/(?:(?P<updated_at>\d{4}\.\d{2}\.\d{2} \d{2}:\d{2}:\d{2}:\d+)|.*)$"
TOC_EXP = re.compile(TOC_RE, re.MULTILINE)


def get_entries(toc: str):
    return TOC_EXP.finditer(toc)


def validate_re(toc):
    entries = list(get_entries(toc))
    lines = toc.split("\n")[2:-1]  # Ignore first two lines (js definitions) and last line (empty newline)
    print(f"{len(entries) == len(lines)} ({len(entries)}/{len(lines)}")
    if len(entries) == len(lines):
        return
    i = j = 0
    while i < len(entries) and j < len(lines):
        if entries[i][0] != lines[j]:
            print(f"e[{i}] != l[{j}] (\"{entries[i][0][:-1]}\" != \"{lines[j][:-1]}\"")
            j += 1
        else:
            i += 1
            j += 1


@dataclass
class TOCObject:
    id: str
    url: str | None
    updated_at: datetime | None


@dataclass
class Meeting(TOCObject):
    number: str
    date: date
    children = {}


@dataclass
class Item(TOCObject):
    parent: Union[Meeting, "Item"]
    item_id: str
    year: int | None
    number: int | None
    title: str
    children = {}


@dataclass
class Speaker:
    salutation: str | None
    name: str
    party: str
    speeches = {}


@dataclass
class Speech(TOCObject):
    parent: Item
    speaker: Speaker
    mp3_url: str | None = None


class TOCFactory:
    def __init__(self):
        self.meetings = {}
        self.items = {}
        self.speakers = {}
        self.speeches = {}

    def parse(self, m: re.Match):
        gps = m.groups()
        id_str = m.group('id')
        url = m.group('url')
        updated_at = m.group("updated_at")
        levels = id_str.split('.')
        if len(levels) == 1:
            level = levels[0]

            if level == "Top":
                print(f"[Top]: {m.groups()}")
            else:
                meet_nr = m.group("meet_nr")
                meet_date = datetime.strptime(m.group("meet_date"), "%d.%m.%Y")
                meeting = Meeting(id_str, url, updated_at, meet_nr, meet_date)
                self.meetings[meeting.id] = meeting
        elif len(levels) >= 2:
            if m.group("item_announcements") or m.group("item_id") or m.group("item_misc"):
                if len(levels) == 2:
                    parent = self.meetings[levels[0]]
                else:
                    parent = self.items['.'.join(levels[:-1])]
                if m.group("item_announcements"):
                    item_id = item_title = m.group("item_announcements")
                    item_year = item_number = None
                elif m.group("item_id"):
                    item_id = m.group("item_id")
                    item_year = int(m.group("item_year")) if m.group("item_year") else None
                    item_number = int(m.group("item_number")) if m.group("item_number") else None
                    item_title = m.group("item_title")
                elif m.group("item_misc"):
                    item_id = item_title = m.group("item_misc")
                    item_year = item_number = None
                else:
                    raise NotImplementedError()
                item = Item(id_str, url, updated_at, parent, item_id, item_year, item_number, item_title)
                self.items[item.id] = item
                parent.children[levels[-1]] = item
            elif m.group("speaker_name"):
                parent = self.items['.'.join(levels[:-1])]
                speaker_salutation = m.group("speaker_salutation")
                speaker_name = m.group("speaker_name")
                speaker_party = m.group("speaker_party")
                speaker = self.find_speaker(speaker_salutation, speaker_name, speaker_party)
                if not speaker:
                    speaker = Speaker(speaker_salutation, speaker_name, speaker_party)
                    self.speakers[f"{speaker_name} ({speaker_party})"] = speaker
                mp3_url = BASE_URL + url.replace("content", "audio").replace("_", " ").replace(".html#Audio-PC ", "_").replace("Audio-PC ", "") + ".mp3"
                speech = Speech(id_str, url, updated_at, parent, speaker, mp3_url)
                # TODO: Download speech audio
                self.speeches[speech.id] = speech

                parent.children[levels[-1]] = speech
                speaker.speeches[speech.id] = speech
        else:
            raise NotImplementedError()
        print("done")


    def find_speaker(self, speaker_salutation: str | None, speaker_name: str, speaker_party: str):
        speaker_id = f"{speaker_name} ({speaker_party})"
        if speaker_id not in self.speakers:
            return None
        speaker = self.speakers[speaker_id]
        # assert speaker.salutation == speaker_salutation
        assert speaker.name == speaker_name
        assert speaker.party == speaker_party
        return speaker


def main():
    toc_url = BASE_URL + "script/tocTab.js"
    r = requests.get(toc_url)
    r.raise_for_status()  # FIXME: handle non OK responses gracefully
    toc = r.text
    validate_re(toc)

    fac = TOCFactory()

    for m in get_entries(toc):
        fac.parse(m)

    for s_k, s in fac.speeches.items():
        p = s.mp3_url.replace("https://audio.gemeinderat-zuerich.ch/audio/", "")
        s_dir, s_file = os.path.split(p)
        dl_dir = os.path.join("dl", s_dir)
        dl_f = os.path.join(dl_dir, s_file)
        if not os.path.isfile(dl_f):
            print(f"[D] {s_k}: {s.mp3_url} -> {dl_f}")
            if not os.path.isdir(dl_dir):
                os.mkdir(dl_dir)
            with requests.get(s.mp3_url, stream=True) as r:
                with open(dl_f, 'wb') as f:
                    shutil.copyfileobj(r.raw, f)
        else:
            print(f"[C] {s_k}: {s.mp3_url} -> {dl_f}")

    files = {}
    for e in get_entries(toc):
        level = e.group('level')
        levels = lvl_rest = level.split('.')
        lvl_files = files
        lvl_cur = "Unknown"
        while lvl_rest:
            lvl_cur, lvl_rest = lvl_rest[0], lvl_rest[1:]
            if lvl_rest:
                lvl_files = lvl_files[lvl_cur][1]
            else:
                lvl_files[lvl_cur] = (e, {})
    print(list(get_entries(toc)))


# https://audio.gemeinderat-zuerich.ch/audio/Sitzung_002_vom_11.05.2022/1652103905677_1652281839835.mp3
# https://audio.gemeinderat-zuerich.ch/audio/Sitzung 002 vom 11.05.2022/1652103905694_1652282931038.mp3

    """
curl 'https://audio.gemeinderat-zuerich.ch/script/tocTab.js' \
  -H 'authority: audio.gemeinderat-zuerich.ch' \
  -H 'accept: */*' \
  -H 'accept-language: en-CH,en;q=0.9,de-CH;q=0.8,de;q=0.7,en-GB;q=0.6,en-US;q=0.5' \
  -H 'cache-control: no-cache' \
  -H 'cookie: SCDID_S=PI9I5ywW3csyqXkQEP3p1tdhR6rDPP_rIfyzxUtWfwrnUqYd8amITw$$#ovY7J6M7XzVzAQEiuxUhCyltHYxL2xmb' \
  -H 'dnt: 1' \
  -H 'pragma: no-cache' \
  -H 'referer: https://audio.gemeinderat-zuerich.ch/' \
  -H 'sec-ch-ua: " Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "macOS"' \
  -H 'sec-fetch-dest: script' \
  -H 'sec-fetch-mode: no-cors' \
  -H 'sec-fetch-site: same-origin' \
  -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36' \
  --compressed"""

if __name__ == "__main__":
    main()