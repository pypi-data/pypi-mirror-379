from __future__ import annotations

from dataclasses import dataclass, is_dataclass
from typing import (
    TYPE_CHECKING,
    Any,
    Callable,
    Generator,
    Iterable,
    Literal,
    Mapping,
    Protocol,
    Self,
    Sequence,
    TypedDict,
    cast,
    get_type_hints,
    overload,
)

from cachetools import LRUCache, cached
from pydantic import BaseModel
from sqlalchemy import delete, func, insert, select, update
from typing_inspection.introspection import AnnotationSource, inspect_annotation

from .engine import get_connection

if TYPE_CHECKING:
    from sqlalchemy import CursorResult
    from sqlalchemy.sql._typing import (
        _ColumnExpressionArgument,
        _ColumnsClauseArgument,
        _JoinTargetArgument,
        _OnClauseArgument,
    )
    from sqlalchemy.sql.dml import (  # type:ignore[attr-defined]
        Delete,
        Executable,
        Insert,
        Select,
        Update,
    )

    from .models import Model

    type ColumnExpression[T] = _ColumnExpressionArgument[T]
    type SelectExpression[T] = _ColumnsClauseArgument[T]
    type Serializer[T] = Callable[..., T]
    type ReturningExecutable = Update | Insert | Delete


TypedDictType = type(TypedDict("_X", {}))  # type:ignore


if TYPE_CHECKING:

    class SupportsPrefetch(Protocol):
        @classmethod
        async def apply_prefetch(
            cls,
            prefetch: Prefetch,
            mapping: Mapping[int, dict[str, Any]],
            ids: Sequence[int],
        ) -> None: ...


@dataclass(slots=True, frozen=True)
class Prefetch:
    key: str
    model: type[SupportsPrefetch]
    select: Sequence[SelectExpression[Any]] | None = None
    order_by: Sequence[ColumnExpression[Any]] | None = None
    mapper: Callable[[Any], Any] | None = None
    many: bool = True


if TYPE_CHECKING:

    class SupportsGenericModel(Protocol):
        @classmethod
        @overload
        def select(
            cls,
            _col: Literal[True] = True,
            /,
            _columns: SelectExpression[Any] | None = None,
        ) -> SelectPlainExecutor: ...

        @classmethod
        @overload
        def select(
            cls,
            _col: Sequence[SelectExpression[Any]],
            /,
            _columns: SelectExpression[Any] | None = None,
        ) -> SelectPlainExecutor: ...

        @classmethod
        @overload
        def select[T](
            cls,
            _col: type[T],
            /,
            _columns: SelectExpression[Any] | None = None,
        ) -> SelectModelExecutor[T]: ...

        @classmethod
        def select(
            cls: type[Any],
            _col: Any = True,
            /,
            _columns: SelectExpression[Any] | None = None,
        ) -> Any: ...

        @classmethod
        def insert(cls: type[Any], **values: Any) -> InsertExecutor: ...

        @classmethod
        def update(cls: type[Any], **values: Any) -> UpdateExecutor: ...

        @classmethod
        def delete(cls: type[Any]) -> DeleteExecutor: ...


class GenericMixin:
    @classmethod
    @overload
    def select(
        cls,
        _col: Literal[True] = True,
        /,
        _columns: SelectExpression[Any] | None = None,
    ) -> SelectPlainExecutor: ...

    @classmethod
    @overload
    def select(
        cls,
        _col: Sequence[SelectExpression[Any]],
        /,
        _columns: SelectExpression[Any] | None = None,
    ) -> SelectPlainExecutor: ...

    @classmethod
    @overload
    def select[T](
        cls,
        _col: type[T],
        /,
        _columns: SelectExpression[Any] | None = None,
    ) -> SelectModelExecutor[T]: ...

    @classmethod
    def select(
        cls: type[Any],
        _col: Any = True,
        /,
        _columns: SelectExpression[Any] | None = None,
    ) -> Any:
        outer = (_columns,) if _columns is not None else ()
        if _col is True:
            return SelectPlainExecutor(cls, select(cls, *outer))
        if isinstance(_col, (list, tuple)):
            return SelectPlainExecutor(
                cls,
                select(*_col, *outer),
            )
        cols, serializer = _get_returning_info(cls, _col)
        return SelectModelExecutor(
            cls,
            select(*cols, *outer),
            serializer,
        )

    @classmethod
    def insert(cls: type[Any], **values: Any) -> InsertExecutor:
        return InsertExecutor(cls, insert(cls).values(**values))

    @classmethod
    def update(cls: type[Any], **values: Any) -> UpdateExecutor:
        return UpdateExecutor(cls, update(cls).values(**values))

    @classmethod
    def delete(cls: type[Any]) -> DeleteExecutor:
        return DeleteExecutor(cls, delete(cls))


class ReturningObjectError(Exception):
    pass


class ObjectDoesNotExist(ReturningObjectError):
    pass


class MultipleObjectsReturned(ReturningObjectError):
    pass


@cached(LRUCache(1024))
def _get_returning_info[T](
    cls: type[Model], arg: type[T]
) -> tuple[list[Any], Serializer[T]]:
    if isinstance(arg, type):
        columns = cls.__table__.columns
        if is_dataclass(arg):
            fields = [
                getattr(cls, field)
                for field in arg.__dataclass_fields__
                if field in columns
            ]
            return fields, cast("Serializer[T]", lambda d: arg(**d))
        if isinstance(arg, TypedDictType):
            fields = [
                getattr(cls, field) for field in get_type_hints(arg) if field in columns
            ]
            return fields, cast("Serializer[T]", dict)
        if issubclass(arg, BaseModel):
            field_keys = [
                (
                    str(field.validation_alias or key)
                    if field.alias_priority == 2
                    else key
                )
                for key, field in arg.model_fields.items()
            ]
            fields = [getattr(cls, field) for field in field_keys if field in columns]
            return fields, cast("Serializer[T]", arg.model_validate)
    raise TypeError(f"Invalid returning class {arg}")


def get_model_executor(executor: Any, inst: StmtExecutor[Any, Any], t: Any, /) -> Any:
    if isinstance(t, TypedDictType):
        return inst
    if isinstance(t, type):
        if issubclass(t, BaseModel):
            return executor(inst._model, inst._stmt, t.model_validate)
        elif issubclass(t, Mapping):
            executor(inst._model, inst._stmt, t)
        else:
            return executor(inst._model, inst._stmt, lambda d: t(**d))
    elif callable(t):
        return executor(inst._model, inst._stmt, t)
    raise TypeError(f"Invalid type {t}")


def check_one_result(model: type[Model], rowcount: int) -> None:
    if rowcount != 1:
        raise (
            model.DoesNotExist("Object does not exist")
            if rowcount == 0
            else model.MultipleReturned(f"Multiple objects returned: {rowcount}")
        )


def clone[F: Callable[..., Any]](meth: F) -> F:
    def wrapper(self: object, *args: Any, **kwds: Any) -> Any:
        cls = self.__class__
        inst = cls.__new__(cls)
        inst.__dict__.update(self.__dict__)
        return meth(inst, *args, **kwds)

    return cast(F, wrapper)


class StmtExecutor[Stmt_T: Executable, Ret_T]:
    def __init__(self, model: type[Model], stmt: Stmt_T) -> None:
        self._model = model
        self._stmt = stmt

    def __await__(self) -> Generator[Any, Any, Ret_T]:
        return self._execute().__await__()

    def _get_stmt(self) -> Executable:
        return self._stmt

    async def _execute(self) -> Ret_T:
        async with get_connection() as conn:
            return await self._serialize(await conn.execute(self._get_stmt()))

    async def _serialize(self, result: CursorResult[Any]) -> Ret_T:
        raise NotImplementedError()


async def serialize_result[T](
    result: CursorResult[Any],
    serializer: Serializer[T],
    prefetch: Sequence[Prefetch] | None,
) -> Sequence[T]:
    if prefetch:
        items = [dict(x) for x in result.mappings().all()]
        mapping = {x.pop("__id"): x for x in items}
        ids = list(mapping)
        for p in prefetch:
            await p.model.apply_prefetch(p, mapping, ids)
        return [serializer(x) for x in items]
    else:
        return [serializer(x) for x in result.mappings().all()]


class SelectExecutor[Ret_T](StmtExecutor["Select[Any]", Sequence[Ret_T]]):
    _prefetch: tuple[Prefetch, ...] | None = None
    _serializer: Serializer[Ret_T]

    def _get_stmt(self) -> Executable:
        if self._prefetch:
            return self._stmt.add_columns(self._model.id.label("__id"))
        return self._stmt

    async def _serialize(self, result: CursorResult[Any]) -> Sequence[Ret_T]:
        return await serialize_result(result, self._serializer, self._prefetch)

    @clone
    def prefetch(self, *items: Prefetch) -> Self:
        if self._prefetch:
            self._prefetch += tuple(items)
        else:
            self._prefetch = items
        return self

    @clone
    def where(self, *clause: ColumnExpression[bool]) -> Self:
        self._stmt = self._stmt.where(*clause)
        return self

    @clone
    def join(
        self,
        target: _JoinTargetArgument,
        onclause: _OnClauseArgument | None = None,
        *,
        isouter: bool = False,
        full: bool = False,
    ) -> Self:
        self._stmt = self._stmt.join(target, onclause, isouter=isouter, full=full)
        return self

    @clone
    def order_by(self, *clauses: ColumnExpression[Any]) -> Self:
        self._stmt = self._stmt.order_by(*clauses)
        return self

    @clone
    def group_by(self, *clauses: ColumnExpression[Any]) -> Self:
        self._stmt = self._stmt.group_by(*clauses)
        return self

    @clone
    def having(self, *clauses: ColumnExpression[bool]) -> Self:
        self._stmt = self._stmt.having(*clauses)
        return self

    @clone
    def limit(self, limit: int) -> Self:
        self._stmt = self._stmt.limit(limit)
        return self

    @clone
    def offset(self, offset: int) -> Self:
        self._stmt = self._stmt.offset(offset)
        return self

    async def all(self) -> Sequence[Ret_T]:
        # convenience method
        return await self._execute()

    async def one(self) -> Ret_T:
        stmt = self._get_stmt()
        async with get_connection() as conn:
            result = await conn.execute(stmt)
            check_one_result(self._model, result.rowcount)
            return (await self._serialize(result))[0]

    async def one_or_none(self) -> Ret_T | None:
        stmt = self._get_stmt()
        async with get_connection() as conn:
            result = await conn.execute(stmt)
            if result.rowcount == 0:
                return None
            check_one_result(self._model, result.rowcount)
            return (await self._serialize(result))[0]

    async def slice(self, limit: int, offset: int) -> tuple[int, Sequence[Ret_T]]:
        stmt = cast("Select[Any]", self._get_stmt())
        async with get_connection() as conn:
            count = await conn.execute(select(func.count()).select_from(stmt.subquery()))
            result = await conn.execute(stmt.limit(limit).offset(offset))
            return count.scalar() or 0, await self._serialize(result)


class MappingProxy:
    def __init__(self, kwargs: Mapping[str, Any]) -> None:
        self.__dict__.update(kwargs)

    if TYPE_CHECKING:

        def __getattr__(self, name: str) -> Any: ...

    def __getitem__(self, key: str) -> Any:
        return self.__dict__[key]

    def __iter__(self) -> Iterable[str]:
        return iter(self.__dict__)

    def __contains__(self, item: str) -> bool:
        return item in self.__dict__

    def pop(self, key: str) -> Any:
        return self.__dict__.pop(key)

    def items(self) -> Iterable[tuple[str, Any]]:
        return self.__dict__.items()

    def keys(self) -> Iterable[str]:
        return self.__dict__.keys()

    def values(self) -> Iterable[Any]:
        return self.__dict__.values()

    def __setattr__(self, key: str, value: Any) -> None:
        raise ValueError("Object is faux immutable")


class SelectPlainExecutor(SelectExecutor[MappingProxy]):
    _serializer = MappingProxy

    @overload
    def model[T](self, _t: type[T], /) -> SelectModelExecutor[T]: ...

    @overload
    def model[T](self, _t: Serializer[T], /) -> SelectModelExecutor[T]: ...

    def model(self, _t: Any, /) -> Any:
        return get_model_executor(SelectModelExecutor, self, _t)


class SelectModelExecutor[Ret_T](SelectExecutor[Ret_T]):
    def __init__(
        self, model: type[Model], stmt: Select[Any], serializer: Serializer[Ret_T]
    ):
        self._model = model
        self._stmt = stmt
        self._serializer = serializer


class ReturningOneExecutor[Stmt_T: ReturningExecutable, Ret_T](
    StmtExecutor[Stmt_T, Ret_T]
):
    @overload
    def returning(
        self, _col: Literal[True] | Literal[None] = None, /
    ) -> ReturningOnePlainExecutor[Stmt_T]: ...

    @overload
    def returning(
        self, _col: Sequence[SelectExpression[Any]], /
    ) -> ReturningOnePlainExecutor[Stmt_T]: ...

    @overload
    def returning[T](self, _col: type[T], /) -> ReturningOneModelExecutor[Stmt_T, T]: ...

    def returning(self, _col: Any = None, /) -> Any:
        if _col is True or _col is None:
            return ReturningOnePlainExecutor(
                self._model, self._stmt.returning(self._model)
            )
        if isinstance(_col, (list, tuple)):
            return ReturningOnePlainExecutor(self._model, self._stmt.returning(*_col))
        cols, serializer = _get_returning_info(self._model, _col)
        return ReturningOneModelExecutor(
            self._model, self._stmt.returning(*cols), serializer
        )


class ReturningStmtExecutor[Stmt_T: ReturningExecutable, Ret_T](
    StmtExecutor[Stmt_T, Ret_T]
):
    _prefetch: tuple[Prefetch, ...] | None = None

    def _get_stmt(self) -> Executable:
        if self._prefetch:
            return self._stmt.returning(self._model.id.label("__id"))
        return self._stmt


class ReturningOnePlainExecutor[Stmt_T: ReturningExecutable](
    ReturningStmtExecutor[Stmt_T, MappingProxy]
):
    async def _serialize(self, result: CursorResult[Any]) -> MappingProxy:
        check_one_result(self._model, result.rowcount)
        return (await serialize_result(result, MappingProxy, self._prefetch))[0]

    @clone
    def prefetch(self, *items: Prefetch) -> Self:
        if self._prefetch:
            self._prefetch += tuple(items)
        else:
            self._prefetch = items
        return self

    @overload
    def model[T](self, _t: type[T], /) -> ReturningOneModelExecutor[Stmt_T, T]: ...

    @overload
    def model[T](self, _t: Serializer[T], /) -> ReturningOneModelExecutor[Stmt_T, T]: ...

    def model(self, _t: Any, /) -> Any:
        return get_model_executor(ReturningOneModelExecutor, self, _t)


class ReturningOneModelExecutor[Stmt_T: ReturningExecutable, Ret_T](
    ReturningStmtExecutor[Stmt_T, Ret_T]
):
    def __init__(self, model: type[Model], stmt: Stmt_T, serializer: Serializer[Ret_T]):
        self._model = model
        self._stmt = stmt
        self._serializer = serializer

    async def _serialize(self, result: CursorResult[Any]) -> Ret_T:
        check_one_result(self._model, result.rowcount)
        return (await serialize_result(result, self._serializer, self._prefetch))[0]

    @clone
    def prefetch(self, *items: Prefetch) -> Self:
        if self._prefetch:
            self._prefetch += tuple(items)
        else:
            self._prefetch = items
        return self


class InsertExecutor(ReturningOneExecutor["Insert", None]):
    async def _serialize(self, result: CursorResult[Any]) -> None:
        return None


class ReturningManyExecutor[Stmt_T: ReturningExecutable, Ret_T](
    StmtExecutor[Stmt_T, Ret_T]
):
    @overload
    def returning(
        self, _col: Literal[True] | Literal[None] = None, /
    ) -> ReturningManyPlainExecutor[Stmt_T]: ...

    @overload
    def returning(
        self, _col: Sequence[SelectExpression[Any]], /
    ) -> ReturningManyPlainExecutor[Stmt_T]: ...

    @overload
    def returning[T](
        self, _col: type[T], /
    ) -> ReturningManyModelExecutor[Stmt_T, T]: ...

    def returning(self, _col: Any = None, /) -> Any:
        if _col is True or _col is None:
            return ReturningManyPlainExecutor(
                self._model, self._stmt.returning(self._model)
            )
        if isinstance(_col, (list, tuple)):
            return ReturningManyPlainExecutor(self._model, self._stmt.returning(*_col))
        cols, serializer = _get_returning_info(self._model, _col)
        return ReturningManyModelExecutor(
            self._model, self._stmt.returning(*cols), serializer
        )

    async def one(self) -> int:
        stmt = self._get_stmt()
        async with get_connection() as conn:
            result = await conn.execute(stmt)
            check_one_result(self._model, result.rowcount)
        return 1


class ReturningManyPlainExecutor[Stmt_T: ReturningExecutable](
    ReturningStmtExecutor[Stmt_T, Sequence[MappingProxy]]
):
    async def _serialize(self, result: CursorResult[Any]) -> Sequence[MappingProxy]:
        return await serialize_result(result, MappingProxy, self._prefetch)

    @clone
    def prefetch(self, *items: Prefetch) -> Self:
        if self._prefetch:
            self._prefetch += tuple(items)
        else:
            self._prefetch = items
        return self

    @overload
    def model[T](self, _t: type[T], /) -> ReturningManyModelExecutor[Stmt_T, T]: ...

    @overload
    def model[T](
        self, _t: Serializer[T], /
    ) -> ReturningManyModelExecutor[Stmt_T, T]: ...

    def model(self, _t: Any, /) -> Any:
        return get_model_executor(ReturningManyModelExecutor, self, _t)

    async def one(self) -> MappingProxy:
        stmt = self._get_stmt()
        async with get_connection() as conn:
            result = await conn.execute(stmt)
            check_one_result(self._model, result.rowcount)
            return (await self._serialize(result))[0]


class ReturningManyModelExecutor[Stmt_T: ReturningExecutable, Ret_T](
    ReturningStmtExecutor[Stmt_T, Sequence[Ret_T]]
):
    def __init__(self, model: type[Model], stmt: Stmt_T, serializer: Serializer[Ret_T]):
        self._model = model
        self._stmt = stmt
        self._serializer = serializer

    async def _serialize(self, result: CursorResult[Any]) -> Sequence[Ret_T]:
        return await serialize_result(result, self._serializer, self._prefetch)

    @clone
    def prefetch(self, *items: Prefetch) -> Self:
        if self._prefetch:
            self._prefetch += tuple(items)
        else:
            self._prefetch = items
        return self

    async def one(self) -> Ret_T:
        stmt = self._get_stmt()
        async with get_connection() as conn:
            result = await conn.execute(stmt)
            check_one_result(self._model, result.rowcount)
            return (await self._serialize(result))[0]


class UpdateExecutor(ReturningManyExecutor["Update", int]):
    async def _serialize(self, result: CursorResult[Any]) -> int:
        return result.rowcount

    @clone
    def where(self, *clause: ColumnExpression[bool]) -> Self:
        self._stmt = self._stmt.where(*clause)
        return self


class DeleteExecutor(ReturningManyExecutor["Delete", int]):
    async def _serialize(self, result: CursorResult[Any]) -> int:
        return result.rowcount

    @clone
    def where(self, *clause: ColumnExpression[bool]) -> Self:
        self._stmt = self._stmt.where(*clause)
        return self
