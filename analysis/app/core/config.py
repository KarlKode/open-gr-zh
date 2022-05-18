"""
File with environment variables and general configuration logic.
`SECRET_KEY`, `ENVIRONMENT` etc. map to env variables with the same names.

Pydantic priority ordering:

1. (Most important, will overwrite everything) - environment variables
2. `.env` file in root folder of project
3. Default values

For project name, version, description we use pyproject.toml
For the rest, we use file `.env` (gitignored), see `.env.example`

`DEFAULT_SQLALCHEMY_DATABASE_URL` and `TEST_SQLALCHEMY_DATABASE_URL`:
Both are ment to be validated at the runtime, do not change unless you know
what are you doing. All the two validators do is to build full URI (TCP protocol)
to databases to avoid typo bugs.

See https://pydantic-docs.helpmanual.io/usage/settings/

Note, complex types like lists are read as json-encoded strings.
"""
import os
from pathlib import Path
from typing import Literal, Any

import toml
from pydantic import AnyHttpUrl, BaseSettings, PostgresDsn, validator, HttpUrl, AnyUrl, MissingError

PROJECT_DIR = Path(__file__).parent.parent.parent
PYPROJECT_PATH = PROJECT_DIR / "pyproject.toml"
if not PYPROJECT_PATH.exists():
    PYPROJECT_PATH = Path.cwd() / "pyproject.toml"
PYPROJECT_CONTENT = toml.load(PYPROJECT_PATH)["tool"]["poetry"]


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
    AUDIO_DIR: Path = PROJECT_DIR / "speech_audio"

    # Project information from pyproject.toml
    PROJECT_NAME: str = PYPROJECT_CONTENT["name"]
    VERSION: str = PYPROJECT_CONTENT["version"]
    DESCRIPTION: str = PYPROJECT_CONTENT["description"]

    # Database
    DATABASE_SCHEME: str | None = None
    DATABASE_HOSTNAME: str | None = None
    DATABASE_USER: str | None = None
    DATABASE_PASSWORD: str | None = None
    DATABASE_PORT: str | None = None
    DATABASE_DB: str | None = None
    DATABASE_URL: DatabaseDsn = None

    # Sentry
    SENTRY_DSN: HttpUrl | None = None

    # Validators
    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def _assemble_cors_origins(cls, v: str | list[str]) -> list[str] | str:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    @validator("AUDIO_DIR", pre=True)
    def _validate_dir(cls, v: str) -> str:
        p = Path(v)
        if not p.exists():
            p.mkdir(parents=True, exist_ok=True)
        return v

    @validator("DATABASE_URL", always=True, check_fields=False)
    def _assemble_database_url(cls, v: str | None, values: dict[str, str]) -> str:
        if isinstance(v, str):
            return v
        scheme, host = values.get("DATABASE_SCHEME"), values.get("DATABASE_HOSTNAME")
        if scheme and host:
            path = values.get("DATABASE_DB")
            if path and path[0] != "/":
                path = "/" + path
            return DatabaseDsn.build(
                scheme=scheme,
                user=values.get("DATABASE_USER", None),
                password=values.get("DATABASE_PASSWORD", None),
                host=host,
                port=values.get("DATABASE_PORT", None),
                path=path,
            )
        raise MissingError()

    @validator("SENTRY_DSN", pre=True)
    def _sentry_dsn_can_be_blank(cls, v: str | None) -> str | None:
        if not v or len(v) == 0:
            return None
        return v

    class Config:
        case_sensitive = True
        env_file = f"{PROJECT_DIR}/.env"
        env_file_encoding = 'utf-8'


settings: Settings = Settings()  # type: ignore
DATABASE_CONFIG = {
    "connections": {"default": settings.DATABASE_URL},
    "apps": {
        "models": {
            "models": settings.MODELS + ["aerich.models"],
            "default_connection": "default",
        },
    },
}
