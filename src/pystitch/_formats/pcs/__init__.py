import pystitch.formats

from . import PcsReader

pystitch.formats.register_format(
    "PCS",
    {
        "description": "Pfaff Embroidery Format",
        "extensions": ("pcs",),
        "mimetype": "application/x-pcs",
        "category": "embroidery",
        "reader": PcsReader,
    }
)
