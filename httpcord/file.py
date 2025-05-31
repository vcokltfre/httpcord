import io
import os


__all__: tuple[str, ...] = (
    "File",
)


class File:
    __slots__: tuple[str, ...] = (
        "_description",
        "_filename",
        "_spoiler",
        "_fp",
        "_data",
    )

    def __init__(
        self,
        fp: os.PathLike | io.BufferedIOBase,
        filename: str,
        description: str | None = None,
        spoiler: bool = False,
    ) -> None:
        self._data: bytes | None = None
        self._fp: os.PathLike | io.BufferedIOBase = fp
        self._filename: str = filename
        self._description: str | None = description
        self._spoiler: bool = spoiler

    @property
    def description(self) -> str | None:
        """The description of the file."""
        return self._description

    @property
    def filename(self) -> str:
        """The name of the file."""
        return self._filename

    @property
    def spoiler(self) -> bool:
        """Whether the file is a spoiler."""
        return self._spoiler

    def read(self) -> bytes:
        """Read the file's content."""
        if self._data is not None:
            return self._data
        if isinstance(self._fp, os.PathLike):
            with open(self._fp, "rb") as f:
                self._data = f.read()
                return self._data
        elif isinstance(self._fp, io.BufferedIOBase):
            self._data = self._fp.read()
            return self._data
        else:
            raise TypeError("File pointer must be a PathLike or BufferedIOBase instance.")

