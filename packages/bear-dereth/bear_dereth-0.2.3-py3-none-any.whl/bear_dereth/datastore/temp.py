"""A storage backend using TinyDB or a stdlib JSON storage handler."""

from collections.abc import Generator
from contextlib import contextmanager, suppress
import json
from pathlib import Path
from typing import Any, Self

from bear_dereth.files import FileWatcher
from bear_dereth.freezing import FrozenDict, freeze
from bear_dereth.lru_cache import LRUCache
from bear_dereth.query import QueryProtocol, QueryTest

from .common import DataShape, ValueType
from .models import Document, Table
from .record import SettingsRecord

# TODO: This needs to be retired, this is not a Table, it's a Storage backend
# and should not implement Table interface directly.
# It should be wrapped in a Storage class that implements Table.


class JsonFileStorage(Table):  # FIXME: This is not semantically correct, this is a Storage, not a Table
    """Stdlib-only storage backend using JSON files."""

    def __init__(self, file_path: str | Path, cache_size: int = 10, **kwargs) -> None:
        self.path = Path(file_path)
        self.save_settings: dict[str, Any] = kwargs
        self._data: list[DataShape] = []
        self._query_cache: LRUCache[QueryProtocol, list[Document]] = LRUCache[QueryProtocol, list[Document]](
            capacity=cache_size
        )
        self._load()
        self._file = FileWatcher(self.path)

    def __call__(self) -> Self:
        return self

    def _load(self) -> None:
        """Load data from JSON file."""

        def _json_get(path: Path) -> list:
            if not path.exists():
                path.parent.mkdir(parents=True, exist_ok=True)
                path.touch()
                path.write_text("[]", encoding="utf-8")
                return []
            try:
                with path.open("r") as f:
                    return json.load(f)
            except (json.JSONDecodeError, OSError):
                return []

        frozen_data: tuple[Document, ...] = self.immutable_data

        for record in _json_get(self.path):
            if isinstance(record, dict) and "key" in record and "value" in record:
                output: SettingsRecord[ValueType] = SettingsRecord.model_validate(record)
                doc: Document = output.get_document()
                frozen: FrozenDict = freeze(doc)
                if frozen not in frozen_data:
                    self._data.append(doc)

    @property
    def immutable_data(self) -> tuple[Document, ...]:
        """Get an immutable copy of the data."""
        return freeze(self._data)

    @contextmanager
    def _cache_check(self) -> Generator[None, Any]:
        """Context manager to check for external file changes."""
        if self._file.has_changed:
            self._load()
        yield

    def _save(self) -> None:
        """Save data to JSON file."""

        def save_to_file() -> None:
            with self.path.open("w") as f:
                json.dump(self._data, f, **self.save_settings)

        with suppress(OSError):
            save_to_file()

    def get(self, key: str) -> Any:
        """Get a value by key."""
        with self._cache_check():
            for record in self._data:
                if record.get("key") == key:
                    return record.get("value")
            return None

    def all(self) -> list[DataShape]:
        """Return all records."""
        with self._cache_check():
            return self._data.copy()

    def upsert(self, record: DataShape, query: QueryTest) -> None:
        """Update existing record or insert new one."""
        with self._cache_check():
            rec: SettingsRecord[ValueType] = SettingsRecord.model_validate(record)
            doc: Document = rec.get_document()

            for index, existing_record in enumerate(self._data):
                if query(existing_record):
                    self._data.pop(index)
                    self._add(doc)
                    return
            self._add(doc)

    def _add(self, record: Document) -> None:
        """Add a new record without checking for existing keys."""
        self._data.append(record)
        self._save()

    def set(self, key: str, value: ValueType) -> None:
        """Set a key-value pair using SettingsRecord."""
        with self._cache_check():
            record: SettingsRecord[ValueType] = SettingsRecord(key=key, value=value)
            doc: Document = record.get_document()
            for existing_record in self._data:
                if existing_record.get("key") == key:
                    self._data.remove(existing_record)
                    self._add(doc)
                    return
            self._add(doc)

    def search(self, query: QueryProtocol | Any) -> list[DataShape]:
        """Search records using a callable query function."""
        # TODO: Query caching is temporarily disabled; re-enable when cache invalidation is robust.
        with self._cache_check():
            # FIXME: This could be optimized further by caching individual records.
            return [record for record in self._data if query(record)]

    def contains(self, query: QueryTest) -> bool:
        """Check if any record matches the query."""
        with self._cache_check():
            return any(query(record) for record in self._data)

    def close(self) -> None:
        """Close the storage (save any pending changes)."""
        self._save()


def Database(file_path: Path, **kwargs: Any) -> Table:  # noqa: N802
    """Factory function to create a database backend instance.

    Args:
        file_path (Path): Path to the database file.
        **kwargs: Additional keyword arguments to pass to the database constructor.

    Returns:
        Table: An instance of the database backend, e.g., JsonFileStorage.
    """
    return JsonFileStorage(file_path, **kwargs)


__all__ = ["Database"]
