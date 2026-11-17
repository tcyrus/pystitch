import pystitch.formats

from . import TxtWriter

pystitch.formats.register_format(
    "TXT",
    {
        "description": "txt Format, Text File",
        "extensions": ("txt",),
        "mimetype": "text/plain",
        "category": "debug",
        "writer": TxtWriter,
        "versions": ("default", "embroidermodder"),
    }
)
