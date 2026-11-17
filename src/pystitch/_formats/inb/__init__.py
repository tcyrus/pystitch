import pystitch.formats

from . import InbReader

pystitch.formats.register_format(
    "INB",
    {
        "description": "Inbro Embroidery Format",
        "extensions": ("inb",),
        "mimetype": "application/x-inb",
        "category": "embroidery",
        "reader": InbReader,
    }
)
