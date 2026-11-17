import pystitch.formats

from . import EdrReader, EdrWriter

pystitch.formats.register_format(
    "EDR",
    {
        "description": "Edr Color Format",
        "extensions": ("edr",),
        "mimetype": "application/x-edr",
        "category": "color",
        "reader": EdrReader,
        "writer": EdrWriter,
    }
)
