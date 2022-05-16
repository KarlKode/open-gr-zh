import os

from asgiref.sync import async_to_sync
from tortoise import Tortoise

from app.celery_app import celery_app  # Required


async def init() -> None:
    DATABASE_URL = os.environ.get("DATABASE_URL", "sqlite://db.sqlite")
    TORTOISE_ORM = {
        "connections": {"default": DATABASE_URL},
        "apps": {
            "models": {
                "models": ["app.models", "aerich.models"],
                "default_connection": "default",
            },
        },
    }

    await Tortoise.init(
        config=TORTOISE_ORM,
    )
    # Generate the schema
    await Tortoise.generate_schemas()


async_to_sync(init)()
