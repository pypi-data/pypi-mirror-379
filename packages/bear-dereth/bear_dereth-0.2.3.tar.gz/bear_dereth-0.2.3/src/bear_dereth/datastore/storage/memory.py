"""In-memory storage backend for the datastore."""

# Updated imports for new datastore structure
from bear_dereth.datastore.models import DataShape, Storage


class InMemoryStorage(Storage):
    """Simple in-memory storage backend for testing or temporary data."""

    def __init__(self) -> None:
        """Initialize empty in-memory storage."""
        super().__init__()
        self._data: DataShape | None = None

    def read(self) -> DataShape | None:
        """Read data from memory.

        Returns:
            Stored data or None if empty
        """
        return self._data

    def write(self, data: DataShape) -> None:
        """Write data to memory.

        Args:
            data: Data to store
        """
        self._data = data

    def close(self) -> None:
        """Clear the stored data."""
        if self._data is not None:
            self._data = None

    @property
    def closed(self) -> bool:
        """Check if the storage is closed (empty)."""
        return self._data is None


__all__ = ["InMemoryStorage"]
