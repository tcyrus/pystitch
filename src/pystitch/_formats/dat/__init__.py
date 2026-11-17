import pystitch.formats

from . import DatReader

pystitch.formats.register_format(
    "DAT",
    {
        "description": "Sunstar or Barudan Embroidery Format",
        "extensions": ("dat",),
        "mimetype": "application/x-dat",
        "category": "embroidery",
        "reader": DatReader,
    }
)
