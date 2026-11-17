from typing import BinaryIO

from pystitch.EmbPattern import EmbPattern

from .DstReader import dst_read_stitches


def read(f: BinaryIO, out: EmbPattern, settings=None):
    f.seek(0x100)
    dst_read_stitches(f, out, settings)
