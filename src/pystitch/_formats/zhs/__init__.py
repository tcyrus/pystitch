import pystitch.formats

from . import ZhsReader

pystitch.formats.register_format(
    "ZHS",
    {
        "description": "Zeng Hsing Embroidery Format",
        "extensions": ("zhs",),
        "mimetype": "application/x-zhs",
        "category": "embroidery",
        "reader": ZhsReader
    }
)
