import pystitch.formats

from . import JpxReader

pystitch.formats.register_format(
    "JPX",
    {
        "description": "Janome Embroidery Format",
        "extensions": ("jpx",),
        "mimetype": "application/x-jpx",
        "category": "embroidery",
        "reader": JpxReader,
    }
)
