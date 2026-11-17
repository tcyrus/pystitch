import pystitch.formats

from . import JsonReader, JsonWriter

pystitch.formats.register_format(
    "JSON",
    {
        "description": "Json Export",
        "extensions": ("json",),
        "mimetype": "application/json",
        "category": "debug",
        "reader": JsonReader,
        "writer": JsonWriter,
    }
)
