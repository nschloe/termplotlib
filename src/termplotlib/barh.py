import decimal
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
    val_format: Optional[str] = None,
    force_ascii: bool = False,
):
    partition = _get_partition(vals, max_width)
    partition = np.repeat(partition, bar_width, axis=1)

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
        if val_format is not None:
            cfmt = val_format
        elif np.issubdtype(np.asarray(vals).dtype, float):
            # find max decimal length
            # https://stackoverflow.com/a/6190291/353337
            num_digits = max(
                -decimal.Decimal(str(val)).as_tuple().exponent for val in vals
            )
            max_len = max(len(str(val)) for val in vals)
            cfmt = f"{{:.{num_digits}f}}"
        elif np.issubdtype(np.asarray(vals).dtype, np.integer):
            max_len = max(len(str(val)) for val in vals)
            cfmt = f"{{:{max_len}d}}"
        else:
            cfmt = "{}"
        fmt.append("[" + cfmt + "]")

    fmt.append("{}")
    fmt = "  ".join(fmt)

    out = []
    for k, (val, num_full, remainder) in enumerate(
        zip(vals, partition[0], partition[1])
    ):
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
    return np.array([eighths // 8, eighths % 8])
