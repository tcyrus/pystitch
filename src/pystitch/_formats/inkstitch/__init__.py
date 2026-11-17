import pystitch.formats

from . import InkstitchGcodeWriter

pystitch.formats.register_writer("GCODE", InkstitchGcodeWriter)
