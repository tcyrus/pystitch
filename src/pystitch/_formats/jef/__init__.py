import pystitch.formats

from . import JefReader, JefWriter

pystitch.formats.register_format(
    "JEF",
    {
        "description": "Janome Embroidery Format",
        "extensions": ("jef",),
        "mimetype": "application/x-jef",
        "category": "embroidery",
        "reader": JefReader,
        "writer": JefWriter,
        "read_options": {
            "trim_distance": (None, 3.0, 50.0),
            "trims": (True, False),
            "trim_at": (2, 3, 4, 5, 6, 7, 8),
            "clipping": (True, False),
        },
        "write_options": {
            "trims": (True, False),
            "trim_at": (2, 3, 4, 5, 6, 7, 8),
        },
    }
)
