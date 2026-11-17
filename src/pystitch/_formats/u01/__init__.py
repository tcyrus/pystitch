import pystitch.formats

from . import U01Reader, U01Writer

pystitch.formats.register_format(
    "U01",
    {
        "description": "Barudan Embroidery Format",
        "extensions": ("u00", "u01", "u02"),
        "mimetype": "application/x-u01",
        "category": "embroidery",
        "reader": U01Reader,
        "writer": U01Writer,
    }
)
