import pystitch.formats

from . import BroReader

pystitch.formats.register_format(
    "BRO",
    {
        "description": "Bits & Volts Embroidery Format",
        "extensions": ("bro",),
        "mimetype": "application/x-Bro",
        "category": "embroidery",
        "reader": BroReader,
    }
)
