import pystitch.formats

# from . import ArtReader

pystitch.formats.register_format(
    "ART",
    {
        "description": "Art Embroidery Format",
        "extensions": ("art",),
        "mimetype": "application/x-art",
        "category": "embroidery",
        "metadata": ("name"),
    }
)
