import pystitch.formats

from . import StcReader

pystitch.formats.register_format(
    "STC",
    {
        "description": "Gunold Embroidery Format",
        "extensions": ("stc",),
        "mimetype": "application/x-stc",
        "category": "embroidery",
        "reader": StcReader,
    }
)
