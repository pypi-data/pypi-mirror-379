from __future__ import annotations

import base64
import importlib
import re
from typing import Any, Callable, Iterable, NamedTuple, Sequence

from alembic.autogenerate import comparators, renderers
from alembic.autogenerate.api import AutogenContext
from alembic.operations import MigrateOperation, Operations
from alembic.operations.ops import UpgradeOps
from sqlalchemy import Connection, MetaData, text

from .entities import Entity, PGExtension, PGFunction, PGTrigger
from .models import Model


def model_loader(
    packages: list[str] | None = None,
) -> MetaData:
    if packages:
        for package in packages:
            module = importlib.import_module(package)
            if hasattr(module, "__package__"):
                try:
                    importlib.import_module(f"{module.__package__}.models")
                except ModuleNotFoundError:
                    pass
    return Model.metadata


class EntityOperationBase[T: Entity](MigrateOperation):
    entity_type: type[T]

    def __init__(self, entity: T) -> None:
        self.entity = entity

    @classmethod
    def invoke_operation(cls, operations: Operations, name: str, **kw: Any) -> Any:
        return operations.invoke(cls(cls.entity_type(name, **kw)))

    def get_operation_name(self) -> str:
        return re.sub(r"(?<!^)(?=[A-Z])", "_", self.__class__.__name__).lower()

    def to_diff_tuple(self) -> tuple[Any, ...]:
        return (
            self.get_operation_name(),
            self.entity.schema,
            self.entity.name,
            self.entity.definition,
        )


class EntityOperation[T: Entity](EntityOperationBase[T]):
    @staticmethod
    def get_reverse_op() -> type[EntityOperation[T]]:
        raise NotImplementedError()

    def reverse(self) -> MigrateOperation:
        return self.get_reverse_op()(self.entity)


class ReplaceEntityOperation[T: Entity](EntityOperationBase[T]):
    def __init__(self, entity: T, old_entity: T | None = None) -> None:
        super().__init__(entity)
        self.old_entity = old_entity

    def reverse(self) -> MigrateOperation:
        assert self.old_entity is not None
        return self.__class__(self.old_entity, self.entity)


def _remember(text: str) -> str:
    return base64.b64encode(text.encode()).decode()


def register_renderer[T: EntityOperationBase[Any]](
    arguments: Iterable[str] = ("schema",),
) -> Callable[[type[T]], type[T]]:
    def wrapper(cls: type[T]) -> type[T]:
        def render_operation(
            _autogen_context: AutogenContext, op: EntityOperationBase[Any]
        ) -> str:
            result = f"op.{op.get_operation_name()}({op.entity.name!r}"
            for arg in arguments:
                if arg == "definition":
                    definition = "\n".join(
                        f"    {x!r}"
                        for x in op.entity.definition.splitlines(keepends=True)
                    )
                    result += f", definition=(\n{definition}\n)"
                elif (value := getattr(op.entity, arg, None)) is not None:
                    result += f", {arg}={value!r}"
            result += ")"
            return result

        renderers.dispatch_for(cls)(render_operation)
        return cls

    return wrapper


@register_renderer()
@Operations.register_operation("create_extension", "invoke_operation")
class CreateExtension(EntityOperation[PGExtension]):
    entity_type = PGExtension

    @staticmethod
    def get_reverse_op() -> type[EntityOperation[PGExtension]]:
        return DropExtension


@Operations.implementation_for(CreateExtension)
def create_extension(operations: Operations, operation: CreateExtension) -> None:
    entity = operation.entity
    if entity.schema is not None:
        schema = f" WITH SCHEMA {entity.schema}"
    else:
        schema = ""
    operations.execute(f"CREATE EXTENSION IF NOT EXISTS {entity.name}" + schema)
    operations.execute(
        f"COMMENT ON EXTENSION {entity.name} is '--alembic:({_remember(entity.definition)})'"
    )


@register_renderer()
@Operations.register_operation("drop_extension", "invoke_operation")
class DropExtension(EntityOperation[PGExtension]):
    entity_type = PGExtension

    @staticmethod
    def get_reverse_op() -> type[EntityOperation[PGExtension]]:
        return CreateExtension


@Operations.implementation_for(DropExtension)
def drop_extension(operations: Operations, operation: DropExtension) -> None:
    entity = operation.entity
    operations.execute(f"DROP EXTENSION {entity.name}")


@register_renderer(arguments=("definition", "schema"))
@Operations.register_operation("create_function", "invoke_operation")
class CreateFunction(EntityOperation[PGFunction]):
    entity_type = PGFunction

    @staticmethod
    def get_reverse_op() -> type[EntityOperation[PGFunction]]:
        return DropFunction


@register_renderer(arguments=("definition", "schema"))
@Operations.register_operation("replace_function", "invoke_operation")
class ReplaceFunction(ReplaceEntityOperation[PGFunction]):
    entity_type = PGFunction


@Operations.implementation_for(CreateFunction)
@Operations.implementation_for(ReplaceFunction)
def create_or_replace_function(
    operations: Operations, operation: CreateFunction | ReplaceFunction
) -> None:
    entity = operation.entity
    if entity.schema is not None:
        signature = f"{entity.schema}.{entity.name}"
    else:
        signature = entity.name
    operations.execute(f"CREATE OR REPLACE FUNCTION {signature} {entity.definition}")
    operations.execute(
        f"COMMENT ON FUNCTION {signature} is '--alembic:({_remember(entity.definition)})'"
    )


@register_renderer()
@Operations.register_operation("drop_function", "invoke_operation")
class DropFunction(EntityOperation[PGFunction]):
    entity_type = PGFunction

    @staticmethod
    def get_reverse_op() -> type[EntityOperation[PGFunction]]:
        return CreateFunction


@Operations.implementation_for(DropFunction)
def drop_function(operations: Operations, operation: DropFunction) -> None:
    entity = operation.entity
    if entity.schema is not None:
        signature = f"{entity.schema}.{entity.name}"
    else:
        signature = entity.name
    operations.execute(f"DROP FUNCTION {signature}")


@register_renderer(arguments=("table", "definition", "schema"))
@Operations.register_operation("create_trigger", "invoke_operation")
class CreateTrigger(EntityOperation[PGTrigger]):
    entity_type = PGTrigger

    @staticmethod
    def get_reverse_op() -> type[EntityOperation[PGTrigger]]:
        return DropTrigger


@register_renderer(arguments=("table", "definition", "schema"))
@Operations.register_operation("replace_trigger", "invoke_operation")
class ReplaceTrigger(ReplaceEntityOperation[PGTrigger]):
    entity_type = PGTrigger


@Operations.implementation_for(CreateTrigger)
@Operations.implementation_for(ReplaceTrigger)
def create_or_replace_trigger(
    operations: Operations, operation: CreateTrigger | ReplaceTrigger
) -> None:
    entity = operation.entity
    if entity.schema is not None:
        table_name = f"{entity.schema}.{entity.table}"
    else:
        table_name = entity.table
    operations.execute(f"CREATE OR REPLACE TRIGGER {entity.name} {entity.definition}")
    operations.execute(
        f"COMMENT ON TRIGGER {entity.name} ON {table_name} is '--alembic:({_remember(entity.definition)})'"
    )


@register_renderer(arguments=("table", "schema"))
@Operations.register_operation("drop_trigger", "invoke_operation")
class DropTrigger(EntityOperation[PGTrigger]):
    entity_type = PGTrigger

    @staticmethod
    def get_reverse_op() -> type[EntityOperation[PGTrigger]]:
        return DropTrigger


@Operations.implementation_for(DropTrigger)
def drop_trigger(operations: Operations, operation: DropTrigger) -> None:
    entity = operation.entity
    if entity.schema is not None:
        table_name = f"{entity.schema}.{entity.table}"
    else:
        table_name = entity.table
    operations.execute(f"DROP TRIGGER IF EXISTS {entity.name} ON {table_name}")


def _get_definition(definition: str) -> str:
    return base64.b64decode(definition.encode()).decode()


def get_db_extensions(
    connection: Connection, schemas: list[str], default_schema: str
) -> Iterable[Entity | None]:
    for schema in schemas:
        for row in connection.execute(
            text(
                "select "
                "  e.extname as name "
                "from "
                "  pg_extension e "
                "  left join pg_description d on d.objoid = e.oid "
                "where "
                "  e.extnamespace = (:schema)::regnamespace "
                "  and d.description ~ :regex"
            ),
            {"schema": schema or default_schema, "regex": "--alembic:\\((.*)\\)"},
        ):
            yield PGExtension(row[0], schema=schema)


def get_db_functions(
    connection: Connection, schemas: list[str], default_schema: str
) -> Iterable[Entity | None]:
    for schema in schemas:
        for row in connection.execute(
            text(
                "select "
                "  p.proname as name, "
                "  pg_get_function_arguments(p.oid) as args, "
                "  substring(d.description from :regex) as description "
                "from "
                "  pg_proc p "
                "  left join pg_description d on d.objoid = p.oid "
                "where "
                "  p.pronamespace = (:schema)::regnamespace "
                "  and d.description ~ :regex"
            ),
            {"schema": schema or default_schema, "regex": "--alembic:\\((.*)\\)"},
        ):
            yield PGFunction(
                f"{row[0]}({row[1]})", _get_definition(row[2]), schema=schema
            )


def get_db_triggers(
    connection: Connection, schemas: list[str], default_schema: str
) -> Iterable[Entity | None]:
    for schema in schemas:
        for row in connection.execute(
            text(
                "select "
                "  t.tgname as name, "
                "  c.relname as tablename, "
                "  substring(d.description from :regex) as description "
                "from "
                "  pg_trigger t "
                "  inner join pg_class c on t.tgrelid = c.oid "
                "  left join pg_description d on d.objoid = t.oid "
                "where "
                "  not t.tgisinternal "
                "  and c.relnamespace = (:schema)::regnamespace "
                "  and d.description ~ :regex"
            ),
            {"schema": schema or default_schema, "regex": "--alembic:\\((.*)\\)"},
        ):
            yield PGTrigger(row[0], row[1], _get_definition(row[2]), schema=schema)


class OperationSchema(NamedTuple):
    get_db_entities: Callable[[Connection, list[str], str], Iterable[Entity | None]]
    create_entity: type[EntityOperation[Any]] | None = None
    drop_entity: type[EntityOperation[Any]] | None = None
    replace_entity: type[ReplaceEntityOperation[Any]] | None = None


_operation_schema: dict[type[Entity], OperationSchema] = {
    PGExtension: OperationSchema(get_db_extensions, CreateExtension, DropExtension),
    PGFunction: OperationSchema(
        get_db_functions, CreateFunction, DropFunction, ReplaceFunction
    ),
    PGTrigger: OperationSchema(
        get_db_triggers, CreateTrigger, DropTrigger, ReplaceTrigger
    ),
}


@comparators.dispatch_for("schema")
def compare_entities(
    autogen_context: AutogenContext,
    upgrade_ops: UpgradeOps,
    schemas: list[str],
) -> None:
    connection = autogen_context.connection
    assert connection is not None
    dialect = autogen_context.dialect
    assert dialect is not None
    default_schema = dialect.default_schema_name or ""
    metadata = autogen_context.metadata
    assert metadata is not None

    entities = {}
    if isinstance(metadata, Sequence):
        for m in metadata:
            entities.update(m.info.get("entities", {}))
    else:
        entities.update(metadata.info.get("entities", {}))

    def run_diffs(
        entity_type: type[Entity],
    ) -> tuple[list[MigrateOperation], list[MigrateOperation], list[MigrateOperation]]:
        add_ops: list[MigrateOperation] = []
        drop_ops: list[MigrateOperation] = []
        replace_ops: list[MigrateOperation] = []
        curr_entities = {
            entity.identity: entity
            for entity in list(entities.values())
            if isinstance(entity, entity_type) and entity.schema in schemas
        }
        op_schema = _operation_schema[entity_type]
        db_entities = {
            entity.identity: entity
            for entity in op_schema.get_db_entities(connection, schemas, default_schema)
            if entity
        }
        if op_schema.create_entity:
            for key in set(curr_entities).difference(db_entities):
                add_ops.append(op_schema.create_entity(curr_entities[key]))
        if op_schema.drop_entity:
            for key in set(db_entities).difference(curr_entities):
                drop_ops.append(op_schema.drop_entity(db_entities[key]))
        if op_schema.replace_entity:
            for key in set(curr_entities).intersection(db_entities):
                if curr_entities[key].definition != db_entities[key].definition:
                    replace_ops.append(
                        op_schema.replace_entity(curr_entities[key], db_entities[key])
                    )
        return add_ops, replace_ops, drop_ops

    add_ext_ops, replace_ext_ops, drop_ext_ops = run_diffs(PGExtension)
    add_func_ops, replace_func_ops, drop_func_ops = run_diffs(PGFunction)
    add_trig_ops, replace_trig_ops, drop_trig_ops = run_diffs(PGTrigger)
    upgrade_ops.ops[0:0] = (
        add_ext_ops + replace_ext_ops + add_func_ops + replace_func_ops
    )
    upgrade_ops.ops += add_trig_ops + replace_trig_ops + drop_trig_ops
    upgrade_ops.ops += drop_func_ops + drop_ext_ops
