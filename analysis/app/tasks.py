from asgiref.sync import async_to_sync

from app import utils
from app.models import Speech
from app.celery_app import celery_app


async def _sync_meetings() -> None:
    await utils.sync_meetings()
    speeches_missing = await Speech.filter(mp3_path__isnull=True)
    for speech in speeches_missing:
        sync_speech.apply_async(args=[speech.id])


@celery_app.task(acks_late=True)
def sync_meetings() -> None:
    async_to_sync(_sync_meetings)()


async def _sync_speech(speech_id: int) -> None:
    await utils.sync_speech(speech_id)


@celery_app.task(acks_late=True)
def sync_speech(speech_id: int) -> None:
    async_to_sync(_sync_speech)(speech_id)
