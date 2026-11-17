from collections.abc import Iterable, Iterator
from typing import BinaryIO, Optional, Protocol

from .EmbPattern import EmbPattern


class ReaderPlugin(Protocol):
    @staticmethod
    def read(
        f: BinaryIO,
        out: EmbPattern,
        settings: Optional[dict] = None
    ): ...

class WriterPlugin(Protocol):
    @staticmethod
    def write(
        pattern: EmbPattern,
        f: BinaryIO,
        settings: Optional[dict] = None
    ): ...


ID: list[str] = []
FORMAT: dict[str, dict] = {}
EXTENSION: dict[str, str] = {}
READERS: dict[str, ReaderPlugin] = {}
WRITERS: dict[str, WriterPlugin] = {}

def register_format(id: str, format: dict) -> None:
    id = id.upper()
    if id not in ID:
        ID.append(id)

    extensions = format.get("extensions", ())
    register_extensions(id, extensions)

    reader = format.pop("reader", None)
    if reader is not None:
        register_reader(id, reader)

    writer = format.pop("writer", None)
    if writer is not None:
        register_writer(id, writer)

    FORMAT[id] = format

def register_extension(id: str, extension: str) -> None:
    EXTENSION[extension.lower()] = id.upper()

def register_extensions(id: str, extensions: Iterable[str]) -> None:
    for extension in extensions:
        register_extension(id, extension)

def registered_extensions() -> dict[str, str]:
    return EXTENSION

def register_reader(id: str, reader: ReaderPlugin) -> None:
    READERS[id.upper()] = reader

def register_writer(id: str, writer: WriterPlugin) -> None:
    WRITERS[id.upper()] = writer

def supported_format(id: str) -> dict:
    _modules = {
        "extension": id.lower(),
        "reader": READERS.get(id, None),
        "writer": WRITERS.get(id, None)
    }
    _modules = {
        k: v for k, v in _modules.items()
        if v is not None
    }
    return FORMAT.get(id, {}) | _modules

def supported_formats() -> Iterator[dict]:
    """
    Generates dictionary entries for supported formats. Each entry will
    always have description, extension, mimetype, and category. Reader
    will provide the reader, if one exists, writer will provide the writer,
    if one exists.

    Metadata gives a list of metadata read and/or written by that type.

    Options provides accepted options by the format and their accepted values.
    """
    for id in ID:
        yield supported_format(id)
