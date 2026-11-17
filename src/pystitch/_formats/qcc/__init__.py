import pystitch.formats

from . import QccReader, QccWriter

pystitch.formats.register_format(
    "QCC",
    {
        "description": "Qcc - QuiltEZ",
        "extensions": ("qcc",),
        "mimetype": "text/plain",
        "category": "quilting",
        "reader": QccReader,
        "writer": QccWriter,
    }
)
