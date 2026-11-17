import pystitch.formats

from . import KsmReader

pystitch.formats.register_format(
    "KSM",
    {
        "description": "Pfaff Embroidery Format",
        "extensions": ("ksm",),
        "mimetype": "application/x-ksm",
        "category": "embroidery",
        "reader": KsmReader,
    }
)
