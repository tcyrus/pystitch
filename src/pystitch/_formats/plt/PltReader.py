import re
from io import TextIOWrapper
from typing import BinaryIO, TextIO

from pystitch.EmbPattern import EmbPattern


def read(f: BinaryIO, out: EmbPattern, settings=None):
    _f = TextIOWrapper(f, errors="ignore")
    _read(_f, out, settings)
    _f.flush()
    _f.detach()

def _read(f: TextIO, out: EmbPattern, settings=None):
    for line in f.readlines():
        line = line.strip()
        if line.startswith("PU"):
            try:
                x, y = get_coords(line)
                x = float(x) / 4
                y = float(y) / -4
                out.move_abs(x, y)
                out.stitch_abs(x, y)
            except ValueError:
                pass

        elif line.startswith("PD"):
            try:
                x, y = get_coords(line)
                x = float(x) / 4
                y = float(y) / -4
                out.stitch_abs(x, y)
            except ValueError:
                pass

        elif line.startswith("SP"):
            try:
                pen_num = re.findall(r"\d+", line)[0]
                pen = int(pen_num)
                out.needle_change(pen)
            except IndexError:
                pass

        elif line == "EN":
            break

def get_coords(line):
    return re.findall(r"[-+]?\d+", line)
