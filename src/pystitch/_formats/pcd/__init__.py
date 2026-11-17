import pystitch.formats

from . import PcdReader

pystitch.formats.register_format(
    "PCD",
    {
        "description": "Pfaff Embroidery Format",
        "extensions": ("pcd",),
        "mimetype": "application/x-pcd",
        "category": "embroidery",
        "reader": PcdReader,
    }
)
