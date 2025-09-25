"""TOML storage backend for the datastore."""

import fcntl
from pathlib import Path
import tomllib
from typing import IO, Any

import tomli_w

# Updated imports for new datastore structure
from bear_dereth.datastore.models import DataShape, Storage
from bear_dereth.files import touch


class TomlStorage(Storage):
    """A TOML file storage backend."""

    def __init__(self, filename: str | Path, file_mode: str = "r+", encoding: str = "utf-8") -> None:
        """Initialize TOML storage.

        Args:
            filename: Path to the TOML file
            file_mode: File mode for opening
            encoding: Text encoding to use
        """
        super().__init__()
        self.filename: Path = touch(filename, mkdir=True)
        self.file_mode: str = file_mode
        self.encoding: str = encoding
        self.file_handle: IO[Any] = self.open(self.filename, file_mode, encoding)

    def open(self, filename: Path, file_mode: str = "r+", encoding: str = "utf-8", **kwargs) -> IO[Any]:
        """Open the TOML file handle.

        Args:
            filename: Path to the file
            file_mode: File mode
            encoding: Text encoding
            **kwargs: Additional arguments

        Returns:
            Open file handle
        """
        return open(filename, file_mode, encoding=encoding, **kwargs)

    def read(self) -> DataShape | None:
        """Read data from TOML file.

        Returns:
            Loaded data or None if empty
        """
        with self.file_handle as handle:
            fcntl.flock(handle.fileno(), fcntl.LOCK_SH)
            handle.seek(0)
            try:
                data: DataShape = tomllib.load(handle)
            finally:
                fcntl.flock(handle.fileno(), fcntl.LOCK_UN)
        return data

    def write(self, data: DataShape) -> None:
        """Write data to TOML file.

        Args:
            data: Data to write
        """
        with self.file_handle as handle:
            fcntl.flock(handle.fileno(), fcntl.LOCK_EX)
            try:
                handle.seek(0)
                handle.truncate()
                tomli_w.dump(data, handle)
                handle.flush()  # Force write to disk
            finally:
                fcntl.flock(handle.fileno(), fcntl.LOCK_UN)

    def close(self) -> None:
        """Close the file handle."""
        if not self.closed:
            self.file_handle.close()

    @property
    def closed(self) -> bool:
        """Check if the storage is closed."""
        return self.file_handle.closed


__all__ = ["TomlStorage"]
