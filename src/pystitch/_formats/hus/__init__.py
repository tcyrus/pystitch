import pystitch.formats

from . import HusReader

pystitch.formats.register_format(
    "HUS",
    {
        "description": "Husqvarna Embroidery Format",
        "extensions": ("hus",),
        "mimetype": "application/x-hus",
        "category": "embroidery",
        "reader": HusReader,
    }
)
