import pystitch.formats

from . import IqpReader

pystitch.formats.register_format(
    "IQP",
    {
        "description": "Iqp - Intelliquilter Format",
        "extensions": ("iqp",),
        "mimetype": "application/x-iqp",
        "category": "quilting",
        "reader": IqpReader,
    }
)
