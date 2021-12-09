from __future__ import annotations

import decimal
import numbers

from .helpers import is_unicode_standard_output


def barh(
    vals: list[int],
    labels: list[str] | None = None,
    max_width: int = 40,
    show_vals: bool = True,
    val_format: str | None = None,
    force_ascii: bool = False,
):
    partition = _get_partition(vals, max_width)

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
        elif all(isinstance(val, numbers.Integral) for val in vals):
            max_len = max(len(str(val)) for val in vals)
            cfmt = f"{{:{max_len}d}}"
        elif all(isinstance(val, numbers.Real) for val in vals):
            # find max decimal length
            # https://stackoverflow.com/a/6190291/353337
            num_digits = max(
                -decimal.Decimal(str(val)).as_tuple().exponent for val in vals
            )
            cfmt = f"{{:.{num_digits}f}}"
        else:
            cfmt = "{}"
        fmt.append("[" + cfmt + "]")

    fmt.append("{}")
    fmt = "  ".join(fmt)

    out = []
    for k, (val, num_full, remainder) in enumerate(zip(vals, *partition)):
        data = []
        if labels is not None:
            data.append(str(labels[k]))
        if show_vals:
            data.append(val)

        # Cut off trailing zeros
        data.append("".join([chars[-1]] * num_full + [chars[remainder]]))
        out.append(fmt.format(*data))

    return out


def _get_partition(values: list[int], max_size: int) -> tuple[list[int], list[int]]:
    assert all(val >= 0 for val in values)
    maxval = max(values)
    if maxval == 0:
        maxval = 1

    eighths = [round(val / maxval * max_size * 8) for val in values]
    return [val // 8 for val in eighths], [val % 8 for val in eighths]
