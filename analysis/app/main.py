import logging
import sys

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from tortoise.contrib.fastapi import register_tortoise

from app.api.api import api_router
from app.core.config import settings, DATABASE_CONFIG

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    description=settings.DESCRIPTION,
    openapi_url="/openapi.json",
    docs_url="/",
)
app.include_router(api_router)


def init_logging():
    logger = logging.getLogger("app")
    logger.setLevel(logging.DEBUG)

    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    ch.setFormatter(formatter)

    logger.addHandler(ch)


def init_middlewares(app: FastAPI):
    # Sets all CORS enabled origins
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Guards against HTTP Host Header attacks
    app.add_middleware(TrustedHostMiddleware, allowed_hosts=settings.ALLOWED_HOSTS)


def init_db(app: FastAPI):
    register_tortoise(
        app,
        config=DATABASE_CONFIG,
        generate_schemas=True,
        add_exception_handlers=True,
    )

    # Tortoise ORM logging
    if False:
        fmt = logging.Formatter(
            fmt="%(asctime)s - %(name)s:%(lineno)d - %(levelname)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
        sh = logging.StreamHandler(sys.stdout)
        sh.setLevel(logging.DEBUG)
        sh.setFormatter(fmt)

        # will print debug sql
        logger_db_client = logging.getLogger("db_client")
        logger_db_client.setLevel(logging.DEBUG)
        logger_db_client.addHandler(sh)

        logger_tortoise = logging.getLogger("tortoise")
        logger_tortoise.setLevel(logging.DEBUG)
        logger_tortoise.addHandler(sh)


init_logging()
init_middlewares(app)
init_db(app)
