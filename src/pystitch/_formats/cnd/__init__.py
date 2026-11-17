import pystitch.formats

pystitch.formats.register_format(
    "CND",
    {
        "description": "Melco Condensed Embroidery Format",
        "extensions": ("cnd",),
        "mimetype": "application/x-cnd",
        "category": "embroidery",
    }
)
