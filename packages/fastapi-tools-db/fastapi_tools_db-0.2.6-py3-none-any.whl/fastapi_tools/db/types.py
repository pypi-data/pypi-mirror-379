from datetime import datetime
from typing import Annotated
from uuid import UUID

from sqlalchemy import DateTime
from sqlalchemy.orm import mapped_column

type Scalar = int | str | float | bool | UUID | None
type Json = dict[str, AnyJson]
type AnyJson = Scalar | list[AnyJson] | dict[str, AnyJson]

# Use ID as type
type ID = Annotated[int, mapped_column(primary_key=True)]

# Datetime with timezone
type DateTimeWithTimeZone = Annotated[datetime, mapped_column(DateTime(timezone=True))]
