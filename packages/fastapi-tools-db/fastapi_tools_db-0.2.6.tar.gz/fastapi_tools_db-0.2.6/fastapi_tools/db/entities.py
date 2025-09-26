from typing import Any, Iterable


class Entity:
    __slots__ = (
        "name",
        "definition",
        "schema",
    )

    def __init__(
        self,
        name: str,
        definition: str | Iterable[str] = "",
        schema: str | None = None,
    ):
        self.name = name
        if definition:
            definition = (
                definition if isinstance(definition, str) else "\n".join(definition)
            )
            self.definition = (
                "\n".join(x.strip() for x in definition.splitlines()) + "\n"
            )
        else:
            self.definition = ""
        self.schema = schema

    @property
    def identity(self) -> tuple[Any, ...]:
        return self.__class__.__name__, self.schema, self.name

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.name!r}, {self.definition!r}, {self.schema!r})"


class PGExtension(Entity):
    __slots__ = ()


class PGFunction(Entity):
    __slots__ = ()


class PGTrigger(Entity):
    __slots__ = ("table",)

    def __init__(
        self,
        name: str,
        table: str,
        definition: str | Iterable[str] = "",
        schema: str | None = None,
    ):
        super().__init__(name, definition, schema)
        self.table = table

    @property
    def identity(self) -> tuple[Any, ...]:
        return self.__class__.__name__, self.schema, self.name, self.table
