import pystitch.formats

from . import PcmReader

pystitch.formats.register_format(
    "PCM",
    {
        "description": "Pfaff Embroidery Format",
        "extensions": ("pcm",),
        "mimetype": "application/x-pcm",
        "category": "embroidery",
        "reader": PcmReader,
    }
)
