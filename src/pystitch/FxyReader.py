from typing import BinaryIO

from pystitch.EmbPattern import EmbPattern

from .DszReader import z_stitch_encoding_read


def read(f: BinaryIO, out: EmbPattern, settings=None):
    f.seek(0x100)
    z_stitch_encoding_read(f, out)
