"""JSON storage backends for the datastore.

Provides both low-level JSON storage and the current JsonFileStorage implementation.
"""

import fcntl
import json
from pathlib import Path
from tempfile import NamedTemporaryFile
from typing import IO, Any, Literal

from bear_dereth.datastore.models import DataShape, Storage
from bear_dereth.files import touch

HandleMode = Literal["default", "temp"]


class JsonStorage(Storage):
    """A low-level JSON file storage with file locking and temp handles."""

    def __init__(self, filename: str | Path, file_mode: str = "r+", encoding: str = "utf-8") -> None:
        """Initialize the JSON storage."""
        super().__init__()
        self.filename: Path = touch(filename, mkdir=True)
        self.temp_handle: IO[Any] = self.open(mode="temp", file_mode=file_mode, encoding=encoding)
        self.file_handle: IO[Any] = self.open(self.filename, file_mode, encoding)
        self.handle_map: dict[HandleMode, IO | None] = {"default": self.file_handle, "temp": self.temp_handle}

    def _handle(self, mode: HandleMode = "default") -> IO[Any] | None:
        if mode not in self.handle_map:
            raise ValueError(f"Invalid mode '{mode}'. Valid modes are: {list(self.handle_map.keys())}")
        return self.handle_map.get(mode, self.file_handle)

    def open(
        self,
        filename: Path = Path("/dev/null"),
        file_mode: str = "r+",
        encoding: str = "utf-8",
        mode: str = "default",
        **kwargs,
    ) -> IO[Any]:
        """Open a file handle, either to the specified filename or a temporary file."""
        if mode == "temp":
            return NamedTemporaryFile(delete_on_close=True, mode=file_mode, encoding=encoding, **kwargs)
        return open(filename, file_mode, encoding=encoding, **kwargs)

    def read(self, mode: HandleMode = "default") -> DataShape | None:
        """Read data from the JSON file."""
        handle: IO[Any] | None = self._handle(mode)
        if handle is None:
            return None
        fcntl.flock(handle.fileno(), fcntl.LOCK_SH)
        handle.seek(0)
        try:
            data: DataShape = json.load(handle)
        finally:
            fcntl.flock(handle.fileno(), fcntl.LOCK_UN)
        return data

    def write(self, data: DataShape, mode: HandleMode = "default") -> None:
        """Write data to the JSON file, replacing existing content."""
        handle: IO[Any] | None = self._handle(mode)
        if handle is None:
            raise ValueError(f"No handle for mode '{mode}'")
        fcntl.flock(handle.fileno(), fcntl.LOCK_EX)
        try:
            handle.seek(0)
            handle.truncate(0)  # Clear file
            json.dump(data, handle, indent=4)
            handle.flush()  # Force write to disk
        finally:
            fcntl.flock(handle.fileno(), fcntl.LOCK_UN)

    def close(self) -> None:
        """Close all file handles."""
        if self.closed:
            return
        for mode, handle in self.handle_map.copy().items():
            if handle and not handle.closed:
                handle.close()
                self.handle_map[mode] = None

    @property
    def closed(self) -> bool:
        """Check if all file handles are closed."""
        return all(handle is None or handle.closed for handle in self.handle_map.values())

    def __del__(self) -> None:
        self.close()


__all__ = ["JsonStorage"]
