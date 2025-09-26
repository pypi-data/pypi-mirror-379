from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from psycopg.connection import ConnParam  # type:ignore[attr-defined]
from pydantic import BaseModel, ConfigDict
from sqlalchemy.log import _EchoFlagType
from sqlalchemy.pool import _ResetStyleArgType


class EngineArgs(BaseModel):
    echo: _EchoFlagType | None = None
    echo_pool: _EchoFlagType | None = None
    logging_name: str | None = None
    max_overflow: int | None = None
    pool_logging_name: str | None = None
    pool_pre_ping: bool | None = True
    pool_size: int | None = 10
    pool_recycle: int | None = 600
    pool_reset_on_return: _ResetStyleArgType | None = None
    pool_timeout: float | None = None
    pool_use_lifo: bool | None = None
    query_cache_size: int | None = None
    use_insertmanyvalues: bool | None = None

    model_config = ConfigDict(frozen=True, extra="forbid")


class PostgresConfig(BaseModel):
    hosts: list[str] = ["127.0.0.1"]
    username: str | None = None
    password: str | None = None
    database: str = "postgres"
    engine_args: EngineArgs = EngineArgs()
    connect_args: Mapping[str, ConnParam] = {}
    session_args: Mapping[str, Any] = {}

    model_config = ConfigDict(frozen=True, extra="forbid")
