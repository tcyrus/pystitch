import pystitch.formats

from . import PltReader, PltWriter

pystitch.formats.register_format(
    "PLT",
    {
        "description": "Plt - HPGL",
        "extensions": ("plt",),
        "mimetype": "text/plain",
        "category": "quilting",
        "reader": PltReader,
        "writer": PltWriter,
    }
)
