import pystitch.formats

from . import XxxReader, XxxWriter

pystitch.formats.register_format(
    "XXX",
    {
        "description": "Singer Embroidery Format",
        "extensions": ("xxx",),
        "mimetype": "application/x-xxx",
        "category": "embroidery",
        "reader": XxxReader,
        "writer": XxxWriter,
    }
)
