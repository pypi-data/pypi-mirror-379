"""Common types and utilities for the datastore."""

from collections.abc import MutableMapping
from types import NoneType
from typing import Any, Literal

from bear_dereth.query._common import QueryTest

TypeList = Literal["string", "number", "float", "list", "boolean", "null"]
"""A type alias for the allowed types in settings."""

ValueType = str | int | float | list | bool | NoneType
"""A type alias for the allowed value types in settings."""

PossibleTypes = type[bool] | type[int] | type[float] | type[str] | type[NoneType] | type[list]
"""A type alias for the possible Python types corresponding to ValueType."""

DataShape = dict[str, dict[str, Any]] | MutableMapping
"""A type alias for the data shape used in the storage."""


__all__ = ["DataShape", "PossibleTypes", "QueryTest", "TypeList", "ValueType"]
