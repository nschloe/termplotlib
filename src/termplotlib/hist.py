from typing import List, Optional

import numpy as np

from .barh import _get_partition, barh
from .helpers import is_unicode_standard_output


def hist(
    counts: List[int],
    bin_edges: List[float],
    orientation: str = "vertical",
    max_width: int = 40,
    grid=None,
    bar_width: int = 1,
    strip: bool = False,
    force_ascii: bool = False,
):
    if orientation == "vertical":
        return hist_vertical(
            counts,
            xgrid=grid,
            bar_width=bar_width,
            strip=strip,
            force_ascii=force_ascii,
        )

    assert orientation == "horizontal", f"Unknown orientation '{orientation}'"
    return hist_horizontal(
        counts,
        bin_edges,
        max_width=max_width,
        bar_width=bar_width,
        force_ascii=force_ascii,
    )


def hist_horizontal(
    counts: List[int],
    bin_edges: List[float],
    max_width: int = 40,
    bar_width: int = 1,
    show_bin_edges: bool = True,
    show_counts: bool = True,
    force_ascii: bool = False,
):
    if show_bin_edges:
        labels = [
            f"{bin_edges[k]:+.2e} - {bin_edges[k+1]:+.2e}"
            for k in range(len(bin_edges) - 1)
        ]
    else:
        labels = None

    return barh(
        counts,
        labels=labels,
        max_width=max_width,
        bar_width=bar_width,
        show_vals=show_counts,
        force_ascii=force_ascii,
    )


def hist_vertical(
    counts: List[int],
    max_height: int = 10,
    bar_width: int = 2,
    strip: bool = False,
    xgrid: Optional[List[int]] = None,
    force_ascii: bool = False,
):
    if xgrid is None:
        xgrid = []

    partition = _get_partition(counts, max_height)

    if strip:
        # Cut off leading and trailing rows of 0
        num_head_rows_delete = np.argmax(np.any(partition != 0, axis=0))
        num_tail_rows_delete = np.argmax(np.any(partition != 0, axis=0)[::-1])

        n = partition.shape[1]
        partition = partition[:, num_head_rows_delete : n - num_tail_rows_delete]
    else:
        num_head_rows_delete = 0

    matrix = _get_matrix_of_eighths(partition[0], partition[1], max_height, bar_width)

    if is_unicode_standard_output() and not force_ascii:
        block_chars = [" ", "▁", "▂", "▃", "▄", "▅", "▆", "▇", "█"]
        left_seven_eighths = "▉"
    else:
        block_chars = [" ", "*", "*", "*", "*", "*", "*", "*", "*"]
        left_seven_eighths = "*"

    block_chars = np.array(block_chars)

    out = []
    for row in np.flipud(matrix.T):
        # converts row into block chars
        c = block_chars[row]

        # add grid lines
        for i in xgrid:
            pos = (i - num_head_rows_delete) * bar_width - 1
            if row[pos] == 8 and (pos + 1 == len(row) or row[pos + 1] > 0):
                c[pos] = left_seven_eighths

        out.append("".join(c))

    return out


def _get_matrix_of_eighths(
    nums_full_blocks, remainders, max_size, bar_width: int
) -> np.ndarray:
    """
    Returns a matrix of integers between 0-8 encoding bar lengths in histogram.

    For instance, if one of the sublists is [8, 8, 8, 3, 0, 0, 0, 0, 0, 0], it means
    that the first 3 segments should be graphed with full blocks, the 4th block should
    be 3/8ths full, and that the rest of the bar should be empty.
    """
    matrix = np.zeros((len(nums_full_blocks), max_size), dtype=int)

    for row, num_full_blocks, remainder in zip(matrix, nums_full_blocks, remainders):
        row[:num_full_blocks] = 8
        if num_full_blocks < matrix.shape[1]:
            row[num_full_blocks] = remainder

    return np.repeat(matrix, bar_width, axis=0)
