import pystitch.formats

from . import MaxReader

pystitch.formats.register_format(
    "MAX",
    {
        "description": "Pfaff Embroidery Format",
        "extensions": ("max",),
        "mimetype": "application/x-max",
        "category": "embroidery",
        "reader": MaxReader,
    }
)
