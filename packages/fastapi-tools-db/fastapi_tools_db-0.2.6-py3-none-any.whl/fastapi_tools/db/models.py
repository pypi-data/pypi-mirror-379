from __future__ import annotations

import datetime
import hashlib
import types
import uuid
from typing import (
    TYPE_CHECKING,
    Any,
    ClassVar,
    Literal,
    Mapping,
    Sequence,
    cast,
    get_args,
    get_origin,
)

from sqlalchemy import (
    ARRAY,
    BIGINT,
    UUID,
    BinaryExpression,
    ForeignKey,
    Index,
    MetaData,
    String,
    func,
    text,
)
from sqlalchemy.dialects.postgresql import JSONB, TIME, TIMESTAMP
from sqlalchemy.orm import DeclarativeBase, Mapped, declared_attr, mapped_column
from sqlalchemy.orm.decl_api import DeclarativeAttributeIntercept

from .engine import get_connection
from .entities import Entity, PGExtension, PGFunction, PGTrigger
from .mixins import (
    GenericMixin,
    MultipleObjectsReturned,
    ObjectDoesNotExist,
    Prefetch,
)
from .types import ID, AnyJson, Json


def _default_type_annotation_map() -> dict[Any, Any]:
    annotated_map: dict[Any, Any] = {
        ID: BIGINT,
        int: BIGINT,
        Json: JSONB,
        AnyJson: JSONB,
        datetime.time: TIME,
        datetime.datetime: TIMESTAMP,
        uuid.UUID: UUID,
    }
    for typ in [Any, int, float, str, bool, Json, AnyJson]:
        annotated_map[list[typ]] = JSONB  # type:ignore[valid-type]
        annotated_map[dict[str, typ]] = JSONB  # type:ignore[valid-type]

    return annotated_map


class DeclarativeMeta(DeclarativeAttributeIntercept):
    def __new__(
        cls,
        name: str,
        bases: tuple[type[Any], ...],
        namespace: dict[str, Any],
        abstract: Literal[True] | None = None,
        tablename: str | None = None,
        __declarative_base_model__: bool = False,
        **kwargs: Any,
    ) -> type[Model]:
        if abstract:
            namespace["__abstract__"] = True
        if tablename:
            namespace["__tablename__"] = tablename
        if __declarative_base_model__:
            return cast(
                "type[Model]", super().__new__(cls, name, bases, namespace, **kwargs)
            )
        if Model in bases:
            assert "id" not in namespace and "id" not in namespace["__annotations__"], (
                "Should not define id field directly"
            )
            namespace["__annotations__"]["id"] = Mapped[ID]
        model = cast(
            "type[Model]", super().__new__(cls, name, bases, namespace, **kwargs)
        )
        return model


class Model(
    GenericMixin,
    DeclarativeBase,
    metaclass=DeclarativeMeta,
    __declarative_base_model__=True,
):
    metadata = MetaData(
        naming_convention={
            "ix": "ix_%(table_name)s_%(column_0_N_name)s",
            "uq": "ix_%(table_name)s_%(column_0_N_name)s",
            "ck": "ck_%(table_name)s_`%(constraint_name)s`",
            "fk": "fk_%(table_name)s_%(column_0_N_name)s",
            "pk": "%(table_name)s_pkey",
        }
    )

    type_annotation_map = _default_type_annotation_map()

    DoesNotExist: ClassVar[type[ObjectDoesNotExist]] = ObjectDoesNotExist
    MultipleReturned: ClassVar[type[MultipleObjectsReturned]] = MultipleObjectsReturned

    def __init_subclass__(cls, **kwargs: Any) -> None:
        super().__init_subclass__(**kwargs)
        cls.DoesNotExist = cast(
            type[ObjectDoesNotExist],
            types.new_class("DoesNotExist", (ObjectDoesNotExist,)),
        )
        cls.MultipleReturned = cast(
            type[MultipleObjectsReturned],
            types.new_class("MultipleReturned", (MultipleObjectsReturned,)),
        )

    if TYPE_CHECKING:
        id: Mapped[ID]

    @classmethod
    async def apply_prefetch(
        cls,
        prefetch: Prefetch,
        mapping: Mapping[int, dict[str, Any]],
        ids: Sequence[int],
    ) -> None:
        mapper = prefetch.mapper or default_mapper
        key = prefetch.key
        many = prefetch.many
        for row in (
            await cls.select(
                True if prefetch.select is None else prefetch.select,
                _columns=cls.id.label("__pid"),
            )
            .where(
                cls.id.in_(ids),
            )
            .order_by(cls.id, *(prefetch.order_by or ()))
        ):
            if many:
                mapping[row.pop("__pid")].setdefault(key, []).append(mapper(row))
            else:
                mapping[row.pop("__pid")][key] = mapper(row)


def add_entity(entity: Entity) -> None:
    Model.metadata.info.setdefault("entities", {})[entity.identity] = entity


def escape_like(value: str) -> str:
    return value.replace("\\", "\\\\").replace("%", "\\%").replace("_", "\\_")


class FastSearchMixin:
    __search_fields__: ClassVar[tuple[str, ...]]

    search: Mapped[list[str]] = mapped_column(ARRAY(String))

    @classmethod
    def search_contains(cls, value: str) -> BinaryExpression[bool]:
        return func.unroll(cls.search).like(f"%{escape_like(value.lower())}%")

    @classmethod
    def search_startswith(cls, value: str) -> BinaryExpression[bool]:
        return func.unroll(cls.search).like(f"%\n{escape_like(value.lower())}%")

    @declared_attr.directive
    def __table_args__(cls: type[Model]) -> tuple[Any, ...]:
        column = func.unroll(text("search::text[]"))
        return (
            Index(
                f"ix_{cls.__tablename__}_search",
                column,
                postgresql_ops={str(column): "gin_trgm_ops"},
                postgresql_using="gin",
            ),
        )

    def __init_subclass__(model, *, search_fields: Sequence[str], **kwargs: Any) -> None:
        if not search_fields:
            raise TypeError("search_fields must be provided")
        if not isinstance(search_fields, (list, tuple)):
            raise TypeError("search_fields must be a list or tuple")
        search_fields = sorted(search_fields)
        model.__search_fields__ = tuple(search_fields)

        add_entity(PGExtension("pg_trgm"))
        add_entity(
            PGFunction(
                "unroll(text[])",
                (
                    "returns text as",
                    "$$",
                    "select lower(concat(chr(10), array_to_string($1, chr(10), ''), chr(10)))",
                    "$$ language sql immutable",
                ),
            )
        )

        table_name: str = cast(Model, model).__tablename__
        hashid = hashlib.blake2b(
            repr((table_name, search_fields)).encode(), digest_size=16
        ).hexdigest()
        func_name = f"fastsearch_{hashid}"
        body = "\n".join(
            f"if new.{f} is not null then search := array_append(search, new.{f}); end if;"
            for f in search_fields
        )
        add_entity(
            PGFunction(
                f"{func_name}()",
                (
                    "returns trigger as",
                    "$$",
                    "declare",
                    "search text[];",
                    "begin",
                    f"{body}",
                    "new.search := search;",
                    "return new;",
                    "end;",
                    "$$ language plpgsql",
                ),
            )
        )
        add_entity(
            PGTrigger(
                f"trigger_{func_name}",
                table_name,
                (
                    f"before insert or update on {table_name}",
                    f"for each row execute function {func_name}()",
                ),
            )
        )
        super().__init_subclass__(**kwargs)


def default_mapper(x: Any) -> Any:
    return x


if TYPE_CHECKING:
    from .mixins import SupportsGenericModel


class ManyToMany[ParentT: SupportsGenericModel, ChildT: SupportsGenericModel](
    Model,
    __declarative_base_model__=True,
    abstract=True,
):
    if TYPE_CHECKING:
        pid: Mapped[ID]
        cid: Mapped[ID]

    _parent_model: type[ParentT]
    _child_model: type[ChildT]

    def __init_subclass__(cls, **kwargs: Any) -> None:
        bases = [b for b in cls.__orig_bases__ if get_origin(b) is ManyToMany]  # type:ignore[attr-defined]
        parent, child = get_args(bases[0])
        assert bases, "class MyModel(ManyToMany[ParentModel, ChildModel]): ... expected"
        assert isinstance(parent, type) and issubclass(parent, Model), (
            "Invalid parent type for ManyToMany"
        )
        assert isinstance(child, type) and issubclass(child, Model), (
            "Invalid child type for ManyToMany"
        )
        parent_pk = list(parent.__table__.primary_key)
        child_pk = list(child.__table__.primary_key)

        assert len(parent_pk) == 1
        assert len(child_pk) == 1

        parent_id = getattr(parent, parent_pk[0].name)
        child_id = getattr(child, child_pk[0].name)

        cls.pid = mapped_column(
            ForeignKey(f"{parent.__tablename__}.{parent_id.key}", ondelete="CASCADE"),
            primary_key=True,
        )
        cls.cid = mapped_column(
            ForeignKey(f"{child.__tablename__}.{child_id.key}", ondelete="CASCADE"),
            primary_key=True,
        )
        cls._parent_model = parent
        cls._child_model = child
        super().__init_subclass__(**kwargs)

    @classmethod
    async def apply_prefetch(
        cls,
        prefetch: Prefetch,
        mapping: Mapping[int, dict[str, Any]],
        ids: Sequence[int],
    ) -> None:
        mapper = prefetch.mapper or default_mapper
        key = prefetch.key
        many = prefetch.many
        for row in (
            await cls._child_model.select(
                True if prefetch.select is None else prefetch.select,
                _columns=cls.pid.label("__pid"),
            )
            .join(cls)
            .where(
                cls.pid.in_(ids),
            )
            .order_by(cls.pid, *(prefetch.order_by or ()))
        ):
            if many:
                mapping[row.pop("__pid")].setdefault(key, []).append(mapper(row))
            else:
                mapping[row.pop("__pid")][key] = mapper(row)

    @classmethod
    async def add(cls, parent_id: int, child_id: int, /) -> bool:
        await cls.insert(pid=parent_id, cid=child_id)
        return True

    @classmethod
    async def remove(cls, parent_id: int, child_id: int, /) -> bool:
        return bool(
            await cls.delete().where((cls.pid == parent_id) & (cls.cid == child_id))
        )

    @classmethod
    async def set(cls, parent_id: int, /, values: Sequence[int]) -> None:
        async with get_connection():
            current_ids = [
                row["cid"] for row in await cls.select().where(cls.pid == parent_id)
            ]
            if remove_ids := set(current_ids) - set(values):
                await cls.delete().where(
                    (cls.pid == parent_id) & (cls.cid.in_(remove_ids))
                )
            if add_ids := set(values) - set(current_ids):
                for child_id in add_ids:
                    await cls.insert(pid=parent_id, cid=child_id)
