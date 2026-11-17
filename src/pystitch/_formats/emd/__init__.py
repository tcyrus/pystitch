import pystitch.formats

from . import EmdReader

pystitch.formats.register_format(
    "EMD",
    {
        "description": "Elna Embroidery Format",
        "extensions": ("emd",),
        "mimetype": "application/x-emd",
        "category": "embroidery",
        "reader": EmdReader,
    }
)
