import pystitch.formats

from . import MitReader

pystitch.formats.register_format(
    "MIT",
    {
        "description": "Mitsubishi Embroidery Format",
        "extensions": ("mit",),
        "mimetype": "application/x-mit",
        "category": "embroidery",
        "reader": MitReader,
    }
)
