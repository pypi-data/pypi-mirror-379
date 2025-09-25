"""Core data models and base classes for the datastore."""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Any, Protocol, Self, runtime_checkable

if TYPE_CHECKING:
    from collections.abc import Mapping
    from types import NoneType

    from bear_dereth.datastore.common import DataShape, ValueType


class Document(dict):
    """A document stored in the database.

    This class provides a way to access both a document's content and
    its ID using ``doc.id``.
    """

    def __init__(self, value: Mapping[str, ValueType], doc_id: int) -> NoneType:
        """Initialize the Document with its content and ID.

        Args:
            value: The content of the document as a dictionary.
            doc_id: The unique identifier for the document.
        """
        super().__init__(value)
        self.doc_id: int = doc_id


@runtime_checkable
class Table(Protocol):
    """Protocol for table-like storage interfaces.

    This defines the interface that storage backends should implement
    for Bear's datastore system.
    """

    def __call__(self, *args: Any, **kwargs: Any) -> Self:
        """Make the table callable."""
        raise NotImplementedError("To be overridden!")

    def get(self, key: str) -> Any:
        """Get a value by key."""
        raise NotImplementedError("To be overridden!")

    def set(self, key: str, value: Any) -> None:
        """Set a key-value pair."""
        raise NotImplementedError("To be overridden!")

    def search(self, query: Any) -> list[DataShape]:
        """Search for records matching a query."""
        raise NotImplementedError("To be overridden!")

    def all(self) -> list[DataShape]:
        """Get all records."""
        raise NotImplementedError("To be overridden!")

    def upsert(self, record: DataShape, query: Any) -> None:
        """Update existing record or insert new one."""
        raise NotImplementedError("To be overridden!")

    def contains(self, query: Any) -> bool:
        """Check if any record matches the query."""
        raise NotImplementedError("To be overridden!")

    def close(self) -> None:
        """Close the table/storage."""
        raise NotImplementedError("To be overridden!")


class Storage(ABC):
    """Abstract base class for all storage backends.

    A Storage handles serialization/deserialization of database state
    to/from various backends (files, memory, etc.).
    """

    @abstractmethod
    def read(self) -> DataShape | None:
        """Read the current state from storage.

        Any kind of deserialization should go here.

        Returns:
            Loaded data or None if storage is empty.
        """
        raise NotImplementedError("To be overridden!")

    @abstractmethod
    def write(self, data: DataShape) -> None:
        """Write the current state to storage.

        Any kind of serialization should go here.

        Args:
            data: The current state of the database.
        """
        raise NotImplementedError("To be overridden!")

    @abstractmethod
    def close(self) -> None:
        """Close open file handles or cleanup resources."""

    @property
    @abstractmethod
    def closed(self) -> bool:
        """Check if the storage is closed."""
        raise NotImplementedError("To be overridden!")

    def __getattr__(self, name: str) -> Any:
        """Forward all unknown attribute calls to the underlying storage."""
        return getattr(self, name)


__all__ = ["Document", "Storage", "Table"]
