import pystitch.formats

from . import ColReader, ColWriter

pystitch.formats.register_format(
    "COL",
    {
        "description": "Col Color Format",
        "extensions": ("col",),
        "mimetype": "application/x-col",
        "category": "color",
        "reader": ColReader,
        "writer": ColWriter,
    }
)
