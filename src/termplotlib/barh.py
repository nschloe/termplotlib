from typing import List, Optional

import numpy as np
from numpy.typing import ArrayLike

from .helpers import is_unicode_standard_output


def barh(
    vals: List[int],
    labels: Optional[List[str]] = None,
    max_width: int = 40,
    bar_width: int = 1,
    show_vals: bool = True,
    force_ascii: bool = False,
):
    nums_full, remainders = _get_partition(vals, max_width)
    nums_full = np.repeat(nums_full, bar_width)
    remainders = np.repeat(remainders, bar_width)

    if is_unicode_standard_output() and not force_ascii:
        chars = [" ", "▏", "▎", "▍", "▌", "▋", "▊", "▉", "█"]
    else:
        chars = [" ", "*", "*", "*", "*", "*", "*", "*", "*"]

    fmt = []
    if labels is not None:
        max_len = max(len(str(label)) for label in labels)
        cfmt = f"{{:{max_len}s}}"
        fmt.append(cfmt)

    if show_vals:
        if np.issubdtype(np.asarray(vals).dtype, np.integer):
            max_len = max(len(str(val)) for val in vals)
            cfmt = f"{{:{max_len}d}}"
        else:
            cfmt = "{}"
        fmt.append("[" + cfmt + "]")

    fmt.append("{}")
    fmt = "  ".join(fmt)

    out = []
    for k, (val, num_full, remainder) in enumerate(zip(vals, nums_full, remainders)):
        data = []
        if labels is not None:
            data.append(str(labels[k]))
        if show_vals:
            data.append(val)

        # Cut off trailing zeros
        data.append("".join([chars[-1]] * num_full + [chars[remainder]]))
        out.append(fmt.format(*data))

    return out


def _get_partition(values: ArrayLike, max_size: int):
    values = np.asarray(values)
    assert np.all(values >= 0)
    maxval = np.max(values)
    if maxval == 0:
        maxval = 1

    eighths = np.around(values / maxval * max_size * 8).astype(int)
    return eighths // 8, eighths % 8
