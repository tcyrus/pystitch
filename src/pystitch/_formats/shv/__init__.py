import pystitch.formats

from . import ShvReader

pystitch.formats.register_format(
    "SHV",
    {
        "description": "Husqvarna Viking Embroidery Format",
        "extensions": ("shv",),
        "mimetype": "application/x-shv",
        "category": "embroidery",
        "reader": ShvReader,
    }
)
