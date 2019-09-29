import sys


def create_padding_tuple(padding):
    # self._padding is a 4-tuple: top, right, bottom, left (just like CSS)
    if isinstance(padding, int):
        out = (padding, padding, padding, padding)
    else:
        if len(padding) == 1:
            out = (padding[0], padding[0], padding[0], padding[0])
        elif len(padding) == 2:
            out = (padding[0], padding[1], padding[0], padding[1])
        elif len(padding) == 3:
            out = (padding[0], padding[1], padding[2], padding[1])
        else:
            assert len(padding) == 4
            out = (padding[0], padding[1], padding[2], padding[3])
    return out


def is_unicode_standard_output():
    return hasattr(sys.stdout, "encoding") and sys.stdout.encoding.lower() in (
        "utf-8",
        "utf8",
    )
