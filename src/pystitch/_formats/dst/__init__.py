import pystitch.formats

from . import (
    DsbReader,
    DstReader,
    DstWriter,
    DszReader,
    ExyReader,
    FxyReader,
    GtReader,
    TapReader,
)

pystitch.formats.register_format(
    "DST",
    {
        "description": "Tajima Embroidery Format",
        "extensions": ("dst",),
        "mimetype": "application/x-dst",
        "category": "embroidery",
        "reader": DstReader,
        "writer": DstWriter,
        "read_options": {
            "trim_distance": (None, 3.0, 50.0),
            "trim_at": (2, 3, 4, 5, 6, 7, 8),
            "clipping": (True, False),
        },
        "write_options": {"trim_at": (2, 3, 4, 5, 6, 7, 8)},
        "versions": ("default", "extended"),
        "metadata": ("name", "author", "copyright"),
    }
)

pystitch.formats.register_format(
    "DSB",
    {
        "description": "Tajima(Barudan) Embroidery Format",
        "extensions": ("dsb",),
        "mimetype": "application/x-dsb",
        "category": "embroidery",
        "reader": DsbReader,
    }
)

pystitch.formats.register_format(
    "DSZ",
    {
        "description": "ZSK USA Embroidery Format",
        "extensions": ("dsz",),
        "mimetype": "application/x-dsz",
        "category": "embroidery",
        "reader": DszReader,
    }
)

pystitch.formats.register_format(
    "EXY", # e??, e01
    {
        "description": "Eltac Embroidery Format",
        "extensions": ("e00", "e01", "e02"),
        "mimetype": "application/x-exy",
        "category": "embroidery",
        "reader": ExyReader,
    }
)

pystitch.formats.register_format(
    "FXY", # f??, f01
    {
        "description": "Fortron Embroidery Format",
        "extensions": ("f00", "f01", "f02"),
        "mimetype": "application/x-fxy",
        "category": "embroidery",
        "reader": FxyReader,
    }
)

pystitch.formats.register_format(
    "TAP",
    {
        "description": "Happy Embroidery Format",
        "extensions": ("tap",),
        "mimetype": "application/x-tap",
        "category": "embroidery",
        "reader": TapReader,
    }
)

pystitch.formats.register_format(
    "GT",
    {
        "description": "Gold Thread Embroidery Format",
        "extensions": ("gt",),
        "mimetype": "application/x-exy",
        "category": "embroidery",
        "reader": GtReader,
    }
)
