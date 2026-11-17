import pystitch.formats

from . import ZxyReader

pystitch.formats.register_format(
    "ZXY",
    {
        "description": "ZSK TC Embroidery Format",
        "extensions": ("z00", "z01", "z02"),
        "mimetype": "application/x-zxy",
        "category": "embroidery",
        "reader": ZxyReader,
    }
)
