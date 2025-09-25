"""Settings Manager Module for Bear Utils."""

import atexit
from collections.abc import Callable, Generator
from contextlib import contextmanager
from pathlib import Path
from typing import Any, Self, cast

from bear_dereth.datastore import Database, Table, ValueType
from bear_dereth.files import derive_settings_path
from bear_dereth.query.query_mapping import QueryMapping, where

Query: type[QueryMapping] = QueryMapping


class SettingsManager:
    """A class to manage settings using TinyDB or a stdlib json storage backend."""

    __slots__: tuple = ("db", "file_path", "name")

    def __init__(
        self,
        name: str,
        file_name: str | None = None,
        path: Path | str | None = None,
        indent: int = 4,
        ensure_ascii: bool = False,
    ) -> None:
        """Initialize the SettingsManager with a specific settings name.

        Args:
            name: Name of the settings (used for file and directory naming)
            path: Optional path to the settings file or directory
            file_name: Optional specific file name (overrides name if provided)
            indent: JSON indentation level (default: 4)
            ensure_ascii: Whether to ensure ASCII encoding in JSON (default: False)
        """
        self.name: str = name
        self.file_path: Path = derive_settings_path(name, file_name, path)
        self.db: Table = Database(self.file_path, indent=indent, ensure_ascii=ensure_ascii)
        atexit.register(self.close)

    def __getattr__(self, key: str) -> Any:
        """Handle dot notation access for settings."""
        if key in self.__slots__:
            raise AttributeError(f"'{key}' not initialized")
        if key.startswith("_"):
            raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{key}'")
        return self.get(key)

    def __setattr__(self, key: str, value: Any) -> None:
        """Handle dot notation assignment for settings."""
        if key in self.__slots__:
            object.__setattr__(self, key, value)
            return
        self.set(key=key, value=value)

    def get(self, key: str, default: Any = None) -> Any:
        """Get a setting value."""
        if result := self.db.search(Query().key == key):
            return result[0]["value"]
        return default

    def get_as_type[T: ValueType](self, key: str, to_type: Callable[[ValueType], T], default: Any = None) -> T:
        """Get a setting value and ensure it is of the expected type."""
        value: ValueType = self.get(key, default)
        if isinstance(value, cast("type", to_type)):
            return to_type(value)
        raise TypeError(f"Failed to coerce setting '{key}' to type {to_type} (got {type(value)})")

    def get_all(self) -> dict:
        """Get all settings as a dictionary."""
        return {doc["key"]: doc["value"] for doc in self.db.all()}

    def set(self, key: str, value: Any) -> None:
        """Set a setting value."""
        self.db.upsert({"key": key, "value": value}, Query().key == key)

    def has(self, key: str) -> bool:
        """Check if a setting exists."""
        return self.db.contains(where("key") == key)

    def open(self) -> None:
        """Reopen the settings file after it's been closed/destroyed."""
        self.db = Database(self.file_path, indent=4, ensure_ascii=False)

    def close(self) -> None:
        """Close the database."""
        self.db.close()

    def destroy_settings(self) -> bool:
        """Delete the settings file."""
        if self.file_path.exists():
            self.close()
            self.file_path.unlink()
            return True
        return False

    def keys(self) -> list[str]:
        """Get all setting keys."""
        return list(self.get_all().keys())

    def items(self) -> list[tuple[str, Any]]:
        """Get all setting key-value pairs."""
        return list(self.get_all().items())

    def values(self) -> list[Any]:
        """Get all setting values."""
        return list(self.get_all().values())

    def __len__(self) -> int:
        return len(self.keys())

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type: object, exc_val: object, exc_tb: object) -> None:
        self.close()

    def __contains__(self, key: str) -> bool:
        return self.has(key)

    def __hash__(self) -> int:
        return hash((self.name, self.file_path, tuple(sorted(self.get_all().items()))))

    def __repr__(self) -> str:
        return f"<SettingsManager settings_name='{self.name}'>"

    def __str__(self) -> str:
        return f"SettingsManager for '{self.name}' with {len(self)} settings."


@contextmanager
def settings(name: str, file_name: str | None = None, path: str | Path | None = None) -> Generator[SettingsManager]:
    """Context manager for SettingsManager."""
    sm: SettingsManager = SettingsManager(name, file_name=file_name, path=path)
    try:
        yield sm
    finally:
        sm.close()


__all__ = ["SettingsManager", "settings"]
