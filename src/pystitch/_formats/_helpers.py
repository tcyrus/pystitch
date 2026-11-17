from pystitch.EmbPattern import EmbPattern

from .csv import CsvReader, CsvWriter
from .dst import DstReader, DstWriter
from .exp import ExpReader, ExpWriter
from .gcode import GcodeReader, GcodeWriter
from .iqp import IqpReader
from .jef import JefReader, JefWriter
from .json import JsonReader, JsonWriter
from .pec import PecReader, PecWriter, PesReader, PesWriter
from .plt import PltReader, PltWriter
from .png import PngWriter
from .qcc import QccReader, QccWriter
from .svg import SvgWriter
from .tbf import TbfReader, TbfWriter
from .txt import TxtWriter
from .u01 import U01Reader, U01Writer
from .vp3 import Vp3Reader, Vp3Writer
from .xxx import XxxReader, XxxWriter


def read_dst(f, settings=None, pattern=None):
    """Reads fileobject as DST file"""
    return EmbPattern.read_embroidery(DstReader, f, settings, pattern)

def read_pec(f, settings=None, pattern=None):
    """Reads fileobject as PEC file"""
    return EmbPattern.read_embroidery(PecReader, f, settings, pattern)

def read_pes(f, settings=None, pattern=None):
    """Reads fileobject as PES file"""
    return EmbPattern.read_embroidery(PesReader, f, settings, pattern)

def read_exp(f, settings=None, pattern=None):
    """Reads fileobject as EXP file"""
    return EmbPattern.read_embroidery(ExpReader, f, settings, pattern)

def read_vp3(f, settings=None, pattern=None):
    """Reads fileobject as VP3 file"""
    return EmbPattern.read_embroidery(Vp3Reader, f, settings, pattern)

def read_jef(f, settings=None, pattern=None):
    """Reads fileobject as JEF file"""
    return EmbPattern.read_embroidery(JefReader, f, settings, pattern)

def read_u01(f, settings=None, pattern=None):
    """Reads fileobject as U01 file"""
    return EmbPattern.read_embroidery(U01Reader, f, settings, pattern)

def read_csv(f, settings=None, pattern=None):
    """Reads fileobject as CSV file"""
    return EmbPattern.read_embroidery(CsvReader, f, settings, pattern)

def read_json(f, settings=None, pattern=None):
    """Reads fileobject as JSON file"""
    return EmbPattern.read_embroidery(JsonReader, f, settings, pattern)

def read_gcode(f, settings=None, pattern=None):
    """Reads fileobject as GCode file"""
    return EmbPattern.read_embroidery(GcodeReader, f, settings, pattern)

def read_xxx(f, settings=None, pattern=None):
    """Reads fileobject as XXX file"""
    return EmbPattern.read_embroidery(XxxReader, f, settings, pattern)

def read_tbf(f, settings=None, pattern=None):
    """Reads fileobject as TBF file"""
    return EmbPattern.read_embroidery(TbfReader, f, settings, pattern)

def read_iqp(f, settings=None, pattern=None):
    """Reads fileobject as IQP file"""
    return EmbPattern.read_embroidery(IqpReader, f, settings, pattern)

def read_plt(f, settings=None, pattern=None):
    """Reads fileobject as PLT file"""
    return EmbPattern.read_embroidery(PltReader, f, settings, pattern)

def read_qcc(f, settings=None, pattern=None):
    """Reads fileobject as QCC file"""
    return EmbPattern.read_embroidery(QccReader, f, settings, pattern)

def write_dst(pattern, stream, settings=None):
    """Writes fileobject as DST file"""
    EmbPattern.write_embroidery(DstWriter, pattern, stream, settings)

def write_pec(pattern, stream, settings=None):
    """Writes fileobject as PEC file"""
    EmbPattern.write_embroidery(PecWriter, pattern, stream, settings)

def write_pes(pattern, stream, settings=None):
    """Writes fileobject as PES file"""
    EmbPattern.write_embroidery(PesWriter, pattern, stream, settings)

def write_exp(pattern, stream, settings=None):
    """Writes fileobject as EXP file"""
    EmbPattern.write_embroidery(ExpWriter, pattern, stream, settings)

def write_vp3(pattern, stream, settings=None):
    """Writes fileobject as Vp3 file"""
    EmbPattern.write_embroidery(Vp3Writer, pattern, stream, settings)

def write_jef(pattern, stream, settings=None):
    """Writes fileobject as JEF file"""
    EmbPattern.write_embroidery(JefWriter, pattern, stream, settings)

def write_u01(pattern, stream, settings=None):
    """Writes fileobject as U01 file"""
    EmbPattern.write_embroidery(U01Writer, pattern, stream, settings)

def write_csv(pattern, stream, settings=None):
    """Writes fileobject as CSV file"""
    EmbPattern.write_embroidery(CsvWriter, pattern, stream, settings)

def write_json(pattern, stream, settings=None):
    """Writes fileobject as JSON file"""
    EmbPattern.write_embroidery(JsonWriter, pattern, stream, settings)

def write_txt(pattern, stream, settings=None):
    """Writes fileobject as CSV file"""
    EmbPattern.write_embroidery(TxtWriter, pattern, stream, settings)

def write_gcode(pattern, stream, settings=None):
    """Writes fileobject as Gcode file"""
    EmbPattern.write_embroidery(GcodeWriter, pattern, stream, settings)

def write_xxx(pattern, stream, settings=None):
    """Writes fileobject as XXX file"""
    EmbPattern.write_embroidery(XxxWriter, pattern, stream, settings)

def write_tbf(pattern, stream, settings=None):
    """Writes fileobject as TBF file"""
    EmbPattern.write_embroidery(TbfWriter, pattern, stream, settings)

def write_plt(pattern, stream, settings=None):
    """Writes fileobject as PLT file"""
    EmbPattern.write_embroidery(PltWriter, pattern, stream, settings)

def write_qcc(pattern, stream, settings=None):
    """Writes fileobject as QCC file"""
    EmbPattern.write_embroidery(QccWriter, pattern, stream, settings)

def write_svg(pattern, stream, settings=None):
    """Writes fileobject as DST file"""
    EmbPattern.write_embroidery(SvgWriter, pattern, stream, settings)

def write_png(pattern, stream, settings=None):
    """Writes fileobject as PNG file"""
    EmbPattern.write_embroidery(PngWriter, pattern, stream, settings)
