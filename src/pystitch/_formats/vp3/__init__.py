import pystitch.formats

from . import Vp3Reader, Vp3Writer

pystitch.formats.register_format(
    "VP3",
    {
        "description": "Pfaff Embroidery Format",
        "extensions": ("vp3",),
        "mimetype": "application/x-vp3",
        "category": "embroidery",
        "reader": Vp3Reader,
        "writer": Vp3Writer,
    }
)
