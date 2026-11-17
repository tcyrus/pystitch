import pystitch.formats

from . import InfReader, InfWriter

pystitch.formats.register_format(
    "INF",
    {
        "description": "Inf Color Format",
        "extensions": ("inf",),
        "mimetype": "application/x-inf",
        "category": "color",
        "reader": InfReader,
        "writer": InfWriter,
    }
)
