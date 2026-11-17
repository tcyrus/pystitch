name = "pystitch"

import os

# items available at the top level (e.g. pystitch.read)
from .EmbConstant import *
from .EmbFunctions import *
from .EmbMatrix import EmbMatrix
from .EmbPattern import EmbPattern
from .EmbThread import EmbThread
from .EmbCompress import compress, expand
import pystitch.GenericWriter as GenericWriter

# items available in a sub-heirarchy
# (e.g. pystitch.GraphicsHelper.get_graphic_as_string)
from .GraphicsHelper import get_graphic_as_string

from ._formats._helpers import *
from .formats import registered_extensions, supported_format, supported_formats


get_extension_by_filename = EmbPattern.get_extension_by_filename
read_embroidery = EmbPattern.read_embroidery
write_embroidery = EmbPattern.write_embroidery


def read(file, settings=None, pattern=None):
    """Reads file, assuming type by extension"""

    # Determine filename
    filename = file
    if not isinstance(filename, (str, os.PathLike)):
        filename = getattr(file, "name")

    extension = EmbPattern.get_extension_by_filename(filename)
    extension = extension.lower()

    file_type = None

    id = registered_extensions().get(extension)
    if id is not None:
        file_type = supported_format(id)

    if file_type is None:
        return None

    reader = file_type.get("reader")

    if reader is None:
        return None

    return EmbPattern.read_embroidery(reader, file, settings, pattern)


def write(pattern, file, settings=None):
    """Writes file, assuming type by extension"""

    # Determine filename
    filename = file
    if not isinstance(filename, (str, os.PathLike)):
        filename = getattr(file, "name")

    extension = EmbPattern.get_extension_by_filename(filename)
    extension = extension.lower()

    file_type = None

    id = registered_extensions().get(extension)
    if id is not None:
        file_type = supported_format(id)

    if file_type is None:
        raise IOError(f"Conversion to file type '{extension}' is not supported")

    writer = file_type.get("writer")

    if writer is None:
        raise IOError("No supported writer found.")

    EmbPattern.write_embroidery(writer, pattern, file, settings)

def convert(filename_from, filename_to, settings=None):
    pattern = read(filename_from, settings)
    if pattern is not None:
        write(pattern, filename_to, settings)
