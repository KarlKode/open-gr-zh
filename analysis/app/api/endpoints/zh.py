from fastapi import APIRouter, BackgroundTasks, HTTPException
from fastapi.responses import FileResponse

from app.models import CouncilMember, Meeting, AgendaItem, Speech
from app.schemas.council import CouncilMemberList_Pydantic, CouncilMember_Pydantic
from app.schemas.meeting import (
    MeetingList_Pydantic,
    Meeting_Pydantic,
    AgendaItemList_Pydantic,
    AgendaItem_Pydantic,
    SpeechList_Pydantic,
    Speech_Pydantic,
)
from app import tasks

router = APIRouter()


@router.get("/council")
async def get_council_members():
    return await CouncilMemberList_Pydantic.from_queryset(CouncilMember.all())


@router.get("/council/{member_id}")
async def get_council_member(member_id: int):
    return await CouncilMember_Pydantic.from_queryset(
        CouncilMember.filter(id=member_id).first()
    )


@router.get("/meetings")
async def get_meetings():
    return await MeetingList_Pydantic.from_queryset(Meeting.all())


@router.post("/meetings/sync")
async def sync_meetings(background_tasks: BackgroundTasks):
    background_tasks.add_task(tasks.sync_meetings)
    return "done"


@router.get("/meetings/{meeting_id}")
async def get_meeting(meeting_id: int):
    return await Meeting_Pydantic.from_queryset_single(Meeting.filter(id=meeting_id).first())


@router.get("/items")
async def get_items():
    return await AgendaItemList_Pydantic.from_queryset(AgendaItem.all())


@router.get("/items/{item_id}")
async def get_item(item_id: int):
    return await AgendaItem_Pydantic.from_queryset_single(
        AgendaItem.filter(id=item_id).first()
    )


@router.get("/speeches")
async def get_speeches():
    return await SpeechList_Pydantic.from_queryset(Speech.all())


@router.post("/speeches/sync")
async def sync_speeches(background_tasks: BackgroundTasks):
    # background_tasks.add_task(tasks.sync_speeches)
    await tasks.sync_speeches(background_tasks)
    return "done"


@router.get("/speeches/{speech_id}")
async def get_speech(speech_id: int):
    return await Speech_Pydantic.from_queryset_single(Speech.filter(id=speech_id).first())


@router.get("/speeches/{speech_id}/download")
async def download_speech(speech_id: int):
    s = await Speech.filter(id=speech_id).first()
    if not s or not s.mp3_path:
        detail = f"Speech {speech_id} not found" if not s else f"Speech {speech_id} not available"
        raise HTTPException(status_code=404, detail=detail)
    return FileResponse(s.mp3_path)
