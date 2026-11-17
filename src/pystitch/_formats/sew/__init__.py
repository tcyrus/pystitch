import pystitch.formats

from . import SewReader, SewWriter

pystitch.formats.register_format(
    "SEW",
    {
        "description": "Janome Embroidery Format",
        "extensions": ("sew",),
        "mimetype": "application/x-sew",
        "category": "embroidery",
        "reader": SewReader,
        "writer": SewWriter,
    }
)
