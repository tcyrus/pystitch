import pystitch.formats

from . import NewReader

pystitch.formats.register_format(
    "NEW",
    {
        "description": "Ameco Embroidery Format",
        "extensions": ("new",),
        "mimetype": "application/x-new",
        "category": "embroidery",
        "reader": NewReader,
    }
)
