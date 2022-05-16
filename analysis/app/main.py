import os
import sys

from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from app.models import Meeting, Meeting_Pydantic
from app.tasks import sync_meetings

app = FastAPI()

DATABASE_URL = os.environ.get(
    "DATABASE_URL",
    "sqlite://db.sqlite",
)
TORTOISE_ORM = {
    "connections": {"default": DATABASE_URL},
    "apps": {
        "models": {
            "models": ["app.models", "aerich.models"],
            "default_connection": "default",
        },
    },
}

register_tortoise(
    app,
    config=TORTOISE_ORM,
    generate_schemas=True,
    add_exception_handlers=True,
)


# Tortoise ORM logging
import logging

fmt = logging.Formatter(
    fmt="%(asctime)s - %(name)s:%(lineno)d - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
sh = logging.StreamHandler(sys.stdout)
sh.setLevel(logging.DEBUG)
sh.setFormatter(fmt)

# will print debug sql
logger_db_client = logging.getLogger("db_client")
# logger_db_client.setLevel(logging.DEBUG)
# logger_db_client.addHandler(sh)

logger_tortoise = logging.getLogger("tortoise")
# logger_tortoise.setLevel(logging.DEBUG)
# logger_tortoise.addHandler(sh)


@app.get("/meetings")
async def get_meetings():
    return await Meeting_Pydantic.from_queryset(Meeting.all())


@app.post("/sync")
async def sync():
    sync_meetings.apply_async()
    return "done"
