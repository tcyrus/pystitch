import pystitch.formats

from . import PmvReader, PmvWriter

pystitch.formats.register_format(
    "PMV",
    {
        "description": "Brother Stitch Format",
        "extensions": ("pmv",),
        "mimetype": "application/x-pmv",
        "category": "stitch",
        "reader": PmvReader,
        "writer": PmvWriter,
    }
)
