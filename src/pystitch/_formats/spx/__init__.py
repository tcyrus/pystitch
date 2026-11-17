import pystitch.formats

from . import SpxReader

pystitch.formats.register_format(
    "SPX",
    {
        "description": "Pfaff Embroidery Format",
        "extensions": ("spx"),
        "mimetype": "application/x-spx",
        "category": "embroidery",
        "reader": SpxReader,
    }
)
