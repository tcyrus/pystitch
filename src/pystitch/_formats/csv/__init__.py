import pystitch.formats

from . import CsvReader, CsvWriter

pystitch.formats.register_format(
    "CSV",
    {
        "description": "Comma-separated values",
        "extensions": ("csv",),
        "mimetype": "text/csv",
        "category": "debug",
        "reader": CsvReader,
        "writer": CsvWriter,
        "versions": ("default", "delta", "full"),
    }
)
