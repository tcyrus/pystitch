def get_graphic_as_string(graphic, one="#", zero=" "):
    """Prints graphic object in text."""
    stride = 6
    if isinstance(graphic, tuple):
        stride = graphic[1]
        graphic = graphic[0]

    if isinstance(graphic, str):
        graphic = bytearray(graphic)

    list_string = [
        one if (byte >> i) & 1 else zero for byte in graphic for i in range(0, 8)
    ]
    bit_stride = 8 * stride
    bit_length = 8 * len(graphic)
    return "\n".join(
        "".join(list_string[m : m + bit_stride])
        for m in range(0, bit_length, bit_stride)
    )
