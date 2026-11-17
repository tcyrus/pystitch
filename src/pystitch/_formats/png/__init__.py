import pystitch.formats

from . import PngWriter

pystitch.formats.register_format(
    "PNG",
    {
        "description": "PNG Format, Portable Network Graphics",
        "extensions": ("png",),
        "mimetype": "image/png",
        "category": "image",
        "writer": PngWriter,
        "write_options": {
            "background": (0x000000, 0xFFFFFF),
            "linewidth": (1, 2, 3, 4, 5, 6, 7, 8, 9, 10),
        },
    }
)
