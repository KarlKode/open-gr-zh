"""
File with environment variables and general configuration logic.
`SECRET_KEY`, `ENVIRONMENT` etc. map to env variables with the same names.

Pydantic priority ordering:

1. (Most important, will overwrite everything) - environment variables
2. `.env` file in root folder of project
3. Default values

For project name, version, description we use pyproject.toml
For the rest, we use file `.env` (gitignored), see `.env.example`

`DEFAULT_SQLALCHEMY_DATABASE_URI` and `TEST_SQLALCHEMY_DATABASE_URI`:
Both are ment to be validated at the runtime, do not change unless you know
what are you doing. All the two validators do is to build full URI (TCP protocol)
to databases to avoid typo bugs.

See https://pydantic-docs.helpmanual.io/usage/settings/

Note, complex types like lists are read as json-encoded strings.
"""

from pathlib import Path
from typing import Literal, Any

import toml
from pydantic import AnyHttpUrl, BaseSettings, PostgresDsn, validator, HttpUrl, AnyUrl

PROJECT_DIR = Path(__file__).parent.parent.parent
PYPROJECT_CONTENT = toml.load(f"{PROJECT_DIR}/pyproject.toml")["tool"]["poetry"]


class DatabaseDsn(AnyUrl):
    allowed_schemes = PostgresDsn.allowed_schemes.union({"sqlite"})


class Settings(BaseSettings):
    # Core Settings
    SECRET_KEY: str
    ENVIRONMENT: Literal["DEV", "TEST", "PROD"] = "DEV"
    SECURITY_BCRYPT_ROUNDS: int = 12
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 11520  # 8 days
    REFRESH_TOKEN_EXPIRE_MINUTES: int = 40320  # 28 days
    # BACKEND_CORS_ORIGINS is a JSON-formatted list of origins
    # e.g: '["http://localhost", "http://localhost:4200", "http://local.dockertoolbox.tiangolo.com"]'
    BACKEND_CORS_ORIGINS: list[AnyHttpUrl] = []
    ALLOWED_HOSTS: list[str] = ["localhost"]

    MODELS: list[str] = ["app.models"]

    # Project information from pyproject.toml
    PROJECT_NAME: str = PYPROJECT_CONTENT["name"]
    VERSION: str = PYPROJECT_CONTENT["version"]
    DESCRIPTION: str = PYPROJECT_CONTENT["description"]

    # Database
    DATABASE_SCHEMA: str = "sqlite"
    DATABASE_HOSTNAME: str | None = None
    DATABASE_USER: str | None = None
    DATABASE_PASSWORD: str | None = None
    DATABASE_PORT: str | None = None
    DATABASE_DB: str | None = None
    DATABASE_URI: DatabaseDsn | None
    DATABASE_CONFIG: dict[str, Any] | None

    # Sentry
    SENTRY_DSN: HttpUrl | None = None

    # Validators
    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: str | list[str]) -> list[str] | str:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    @validator("DATABASE_URI")
    def _assemble_database_uri(
        cls, v: str | None, values: dict[str, str]
    ) -> str:
        if isinstance(v, str):
            return v
        if values["DATABASE_SCHEMA"] and values["DATABASE_HOSTNAME"]:
            return DatabaseDsn.build(
                scheme="postgresql+asyncpg",
                user=values["DATABASE_USER"],
                password=values["DATABASE_PASSWORD"],
                host=values["DATABASE_HOSTNAME"],
                port=values["DATABASE_PORT"],
                path=f"/{values['DATABASE_DB']}",
            )
        raise ValueError("DATABASE_URI or DATABASE_* required")

    @validator("DATABASE_CONFIG")
    def _assemble_database_config(cls, v: dict[str, Any] | None, values: dict[str, str | list[str]]) -> dict[str, Any]:
        if v:
            return v
        return {
            "connections": {"default": values["DATABASE_URI"]},
            "apps": {
                "models": {
                    "models": values["MODELS"] + ["aerich.models"],
                    "default_connection": "default",
                },
            },
        }

    @validator("SENTRY_DSN", pre=True)
    def _sentry_dsn_can_be_blank(cls, v: str | None) -> str | None:
        if not v or len(v) == 0:
            return None
        return v

    class Config:
        env_file = f"{PROJECT_DIR}/.env"
        case_sensitive = True


settings: Settings = Settings()  # type: ignore
DATABASE_CONFIG = settings.DATABASE_CONFIG
