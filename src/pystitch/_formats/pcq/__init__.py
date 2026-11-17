import pystitch.formats

from . import PcqReader

pystitch.formats.register_format(
    "PCQ",
    {
        "description": "Pfaff Embroidery Format",
        "extensions": ("pcq",),
        "mimetype": "application/x-pcq",
        "category": "embroidery",
        "reader": PcqReader,
    }
)
