import pystitch.formats

from . import TbfReader, TbfWriter

pystitch.formats.register_format(
    "TBF",
    {
        "description": "Tajima Embroidery Format",
        "extensions": ("tbf",),
        "mimetype": "application/x-tbf",
        "category": "embroidery",
        "reader": TbfReader,
        "writer": TbfWriter,
    }
)
