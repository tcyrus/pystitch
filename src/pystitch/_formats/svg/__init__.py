import pystitch.formats

from . import SvgWriter

pystitch.formats.register_format(
    "SVG",
    {
        "description": "Scalable Vector Graphics",
        "extensions": ("svg", "svgz"),
        "mimetype": "image/svg+xml",
        "category": "vector",
        "writer": SvgWriter,
    }
)
