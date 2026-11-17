import pystitch.formats

from . import GcodeReader

pystitch.formats.register_format(
    "GCODE",
    {
        "description": "gcode Format, Text File",
        "extensions": ("gcode", "g-code", "ngc", "nc", ".g"),
        "mimetype": "text/plain",
        "category": "embroidery",
        "reader": GcodeReader,
        "write_options": {
            "flip_x": (True, False),
            "flip_y": (True, False),
            "alternate_z": (True, False),
            "stitch_z_travel": (int),
        },
    }
)
