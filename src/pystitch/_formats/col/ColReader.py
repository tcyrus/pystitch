from io import TextIOWrapper
from typing import BinaryIO, TextIO

from pystitch.EmbPattern import EmbPattern
from pystitch.EmbThread import EmbThread


def read(f: BinaryIO, out: EmbPattern, settings=None):
    _f = TextIOWrapper(f, errors="ignore")
    _read(_f, out, settings)
    _f.flush()
    _f.detach()

def _read(f: TextIO, out: EmbPattern, settings=None):
    count = int(f.readline())
    for i in range(count):
        line = f.readline()
        splits = line.split(",")
        thread = EmbThread()
        thread.catalog_number = splits[0]
        thread.set_color(int(splits[1]), int(splits[2]), int(splits[3]))
        out.add_thread(thread)
