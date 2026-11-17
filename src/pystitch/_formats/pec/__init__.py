import pystitch.formats

from . import PecReader, PecWriter, PesReader, PesWriter, PhbReader, PhcReader

pystitch.formats.register_format(
    "PEC",
    {
        "description": "Brother Embroidery Format",
        "extensions": ("pec",),
        "mimetype": "application/x-pec",
        "category": "embroidery",
        "reader": PecReader,
        "writer": PecWriter,
        "metadata": ("name"),
    }
)

pystitch.formats.register_format(
    "PES",
    {
        "description": "Brother Embroidery Format",
        "extensions": ("pes",),
        "mimetype": "application/x-pes",
        "category": "embroidery",
        "reader": PesReader,
        "writer": PesWriter,
        "versions": ("1", "6", "1t", "6t"),
        "metadata": ("name", "author", "category", "keywords", "comments"),
    }
)

pystitch.formats.register_format(
    "PHB",
    {
        "description": "Brother Embroidery Format",
        "extensions": ("phb",),
        "mimetype": "application/x-phb",
        "category": "embroidery",
        "reader": PhbReader,
    }
)

pystitch.formats.register_format(
    "PHC",
    {
        "description": "Brother Embroidery Format",
        "extensions": ("phc",),
        "mimetype": "application/x-phc",
        "category": "embroidery",
        "reader": PhcReader,
    }
)
