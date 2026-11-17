import pystitch.formats

from . import A10oReader, A100Reader

pystitch.formats.register_format(
    "10O",
    {
        "description": "Toyota Embroidery Format",
        "extensions": ("10o",),
        "mimetype": "application/x-10o",
        "category": "embroidery",
        "reader": A10oReader,
    }
)

pystitch.formats.register_format(
    "100",
    {
        "description": "Toyota Embroidery Format",
        "extensions": ("100",),
        "mimetype": "application/x-100",
        "category": "embroidery",
        "reader": A100Reader,
    }
)
