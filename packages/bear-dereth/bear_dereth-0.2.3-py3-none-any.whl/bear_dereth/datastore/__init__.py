"""Bear's datastore - A clean, simple, and powerful document storage system.

This module provides a lightweight alternative to TinyDB with Bear's own flavor.
Supports multiple storage backends (JSON, TOML, in-memory) and advanced querying.
"""

from .common import DataShape, ValueType
from .models import Document, Storage
from .record import SettingsRecord
from .temp import Database, JsonFileStorage, Table

__all__ = [
    "DataShape",
    "Database",
    "Document",
    "JsonFileStorage",
    "SettingsRecord",
    "Storage",
    "Table",
    "ValueType",
]
