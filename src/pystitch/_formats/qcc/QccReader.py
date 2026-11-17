import re
from io import TextIOWrapper
from typing import BinaryIO, TextIO

from pystitch.EmbPattern import EmbPattern

TENTH_MM_PER_INCH = 254

def read(f: BinaryIO, out: EmbPattern, settings=None):
    _f = TextIOWrapper(f, errors="ignore")
    _read(_f, out, settings)
    _f.flush()
    _f.detach()

def _read(f: TextIO, out: EmbPattern, settings=None):
    for line in f.readlines():
        line = line.strip()
        if "M02" in line:
            break

        try:
            x, y = get_coords(line)
            x = float(x) * TENTH_MM_PER_INCH
            y = -float(y) * TENTH_MM_PER_INCH
            out.move_abs(x, y)
            out.stitch_abs(x, y)
        except ValueError:
            pass

def get_coords(line):
    return re.findall(r"[X,Y]([-+]?\d+\.\d*)", line)
