from __future__ import annotations

import contextlib
from contextvars import ContextVar
from typing import Any, AsyncIterator

from pydantic import PostgresDsn, TypeAdapter
from sqlalchemy.ext.asyncio import AsyncConnection, AsyncEngine, create_async_engine

from .config import PostgresConfig

__all__ = (
    "AsyncConnection",
    "AsyncEngine",
    "get_connection",
    "get_engine",
    "setup",
)

_shared_conn: ContextVar[AsyncConnection | None] = ContextVar(
    "_shared_conn", default=None
)


class EngineFactory:
    _engine: AsyncEngine

    def setup(self, _config: PostgresConfig | None = None, /, **kwargs: Any) -> None:
        if getattr(self, "_engine", None) is not None:
            raise TypeError("Engine already configured")
        config = (
            TypeAdapter(PostgresConfig)
            .validate_python(
                {**(_config.model_dump(exclude_none=True) if _config else {}), **kwargs}
            )
            .model_dump(exclude_none=True)
        )
        username = config.get("username")
        password = config.get("password")
        url = str(
            PostgresDsn.build(
                scheme="postgresql+psycopg",
                username=username,
                password=password,
                host=",".join(config["hosts"]),
                path=config["database"],
            )
        )
        engine_args = config.get("engine_args") or {}
        connect_args = config.get("connect_args") or {}
        self._engine = create_async_engine(url, **engine_args, connect_args=connect_args)

    def get_engine(self) -> AsyncEngine:
        try:
            return self._engine
        except AttributeError:
            raise RuntimeError("Engine is not configured")

    @contextlib.asynccontextmanager
    async def get_connection(
        self, shared: bool = True
    ) -> AsyncIterator[AsyncConnection]:
        try:
            engine = self._engine
        except AttributeError:
            raise RuntimeError("Engine is not configured")

        if shared:
            conn = _shared_conn.get()
            if conn is not None:
                # using same connection/transaction
                yield conn
            else:
                async with engine.connect() as conn:
                    async with conn.begin():
                        token = _shared_conn.set(conn)
                        try:
                            yield conn
                        finally:
                            _shared_conn.reset(token)
        else:
            async with engine.connect() as conn:
                async with conn.begin():
                    yield conn


factory = EngineFactory()

setup = factory.setup
get_engine = factory.get_engine
get_connection = factory.get_connection

del factory
