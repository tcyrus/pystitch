import json
from io import TextIOWrapper
from typing import BinaryIO, TextIO

from pystitch.EmbFunctions import decode_embroidery_command, get_common_name_dictionary
from pystitch.EmbPattern import EmbPattern

ENCODE = False


def decoded_name(names, data):
    command = decode_embroidery_command(data)
    try:
        name = names[command[0]]
        if command[1] is not None:
            name = name + " t" + str(command[1])
        if command[2] is not None:
            name = name + " n" + str(command[2])
        if command[3] is not None:
            name = name + " o" + str(command[3])
    except (IndexError, KeyError):
        name = "UNKNOWN " + str(data)
    return name

def write(pattern: EmbPattern, f: BinaryIO, settings=None):
    _f = TextIOWrapper(f)
    _write(pattern, _f, settings)
    _f.flush()
    _f.detach()

def _write(pattern: EmbPattern, f: TextIO, settings=None):
    names = get_common_name_dictionary()

    metadata = {}
    for item in pattern.extras.items():
        key, value = item
        if isinstance(value, str):
            metadata[key] = value
        elif isinstance(value, int):
            metadata[key] = value
        elif isinstance(value, float):
            metadata[key] = value

    json_normal = {
        "threadlist": [
            {
                "color": thread.hex_color(),
                "description": thread.description,
                "catalog_number": thread.catalog_number,
                "details": thread.details,
                "brand": thread.brand,
                "chart": thread.chart,
                "weight": thread.weight,
            }
            for thread in pattern.threadlist
        ],
        "stitches": [
            [s[0], s[1], str(decoded_name(names, s[2]))] for s in pattern.stitches
        ],
        "extras": metadata,
    }
    json.dump(json_normal, f, indent=4)
