import pystitch.formats

from . import ExpReader, ExpWriter, StxReader

pystitch.formats.register_format(
    "EXP",
    {
        "description": "Melco Expanded Embroidery Format",
        "extensions": ("exp",),
        "mimetype": "application/x-exp",
        "category": "embroidery",
        "reader": ExpReader,
        "writer": ExpWriter,
    }
)

pystitch.formats.register_format(
    "STX",
    {
        "description": "Data Stitch Embroidery Format",
        "extensions": ("stx",),
        "mimetype": "application/x-stx",
        "category": "embroidery",
        "reader": StxReader,
    }
)
