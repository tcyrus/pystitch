from typing import BinaryIO


def signed8(b: int) -> int:
    if b > 127:
        return -256 + b
    else:
        return b


def signed16(v: int) -> int:
    v &= 0xFFFF
    if v > 0x7FFF:
        return -0x10000 + v
    else:
        return v


def signed24(v: int) -> int:
    v &= 0xFFFFFF
    if v > 0x7FFFFF:
        return -0x1000000 + v
    else:
        return v


def read_signed(stream: BinaryIO, n: int) -> list[int]:
    ba = bytearray(stream.read(n))
    signed_bytes = []
    for b in ba:
        signed_bytes.append(signed8(b))
    return signed_bytes


def read_sint_8(stream: BinaryIO):
    ba = bytearray(stream.read(1))
    if len(ba) != 1:
        return None
    return signed8(ba[0])


def read_int_8(stream: BinaryIO):
    ba = bytearray(stream.read(1))
    if len(ba) != 1:
        return None
    return ba[0]


def read_int_16le(stream: BinaryIO):
    ba = bytearray(stream.read(2))
    if len(ba) != 2:
        return None
    return int.from_bytes(ba, byteorder='little')


def read_int_16be(stream: BinaryIO):
    ba = bytearray(stream.read(2))
    if len(ba) != 2:
        return None
    return int.from_bytes(ba, byteorder='big')


def read_int_24le(stream: BinaryIO):
    ba = bytearray(stream.read(3))
    if len(ba) != 3:
        return None
    return int.from_bytes(ba, byteorder='little')


def read_int_24be(stream: BinaryIO):
    ba = bytearray(stream.read(3))
    if len(ba) != 3:
        return None
    return int.from_bytes(ba, byteorder='big')


def read_int_32le(stream: BinaryIO):
    ba = bytearray(stream.read(4))
    if len(ba) != 4:
        return None
    return int.from_bytes(ba, byteorder='little')


def read_int_32be(stream: BinaryIO):
    ba = bytearray(stream.read(4))
    if len(ba) != 4:
        return None
    return int.from_bytes(ba, byteorder='big')


def read_string_8(stream: BinaryIO, length: int):
    byte = stream.read(length)
    try:
        return byte.decode("utf8")
    except UnicodeDecodeError:
        return None  # Must be > 128 chars.


def read_string_16(stream: BinaryIO, length: int):
    byte = stream.read(length)
    try:
        return byte.decode("utf16")
    except UnicodeDecodeError:
        return None
