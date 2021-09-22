import re
import subprocess
import sys
from typing import List, Tuple, Union


def create_padding_tuple(padding: Union[int, List[int], Tuple[int, int]]):
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
    if sys.stdout.encoding is None:
        return True

    return hasattr(sys.stdout, "encoding") and sys.stdout.encoding.lower() in (
        "utf-8",
        "utf8",
    )


def get_gnuplot_version():
    out = subprocess.check_output(["gnuplot", "--version"]).decode()
    m = re.match("gnuplot (\\d).(\\d) patchlevel (\\d)\n", out)
    if m is None:
        raise RuntimeError("Couldn't get gnuplot version")

    return int(m.group(1)), int(m.group(2)), int(m.group(3))
