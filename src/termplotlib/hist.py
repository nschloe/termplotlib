from typing import List, Optional

import numpy as np
from numpy.typing import ArrayLike

from .barh import barh
from .helpers import is_unicode_standard_output


def _get_matrix_of_eighths(
    counts: ArrayLike, max_size: int, bar_width: int
) -> np.ndarray:
    """
    Returns a matrix of integers between 0-8 encoding bar lengths in histogram.

    For instance, if one of the sublists is [8, 8, 8, 3, 0, 0, 0, 0, 0, 0], it means
    that the first 3 segments should be graphed with full blocks, the 4th block should
    be 3/8ths full, and that the rest of the bar should be empty.
    """
    counts = np.asarray(counts)
    max_count = np.max(counts)

    # translate to eighths of a textbox
    if max_count == 0:
        eighths = np.zeros(len(counts), dtype=int)
    else:
        eighths = np.around(counts / max_count * max_size * 8).astype(int)

    # prepare matrix
    matrix = np.zeros((len(eighths), max_size), dtype=int)
    nums_full_blocks = eighths // 8
    remainders = eighths % 8
    for row, num_full_blocks, remainder in zip(matrix, nums_full_blocks, remainders):
        row[:num_full_blocks] = 8
        if num_full_blocks < matrix.shape[1]:
            row[num_full_blocks] = remainder

    return np.repeat(matrix, bar_width, axis=0)


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

    matrix = _get_matrix_of_eighths(counts, max_height, bar_width)

    if strip:
        # Cut off leading and trailing rows of 0
        num_head_rows_delete = 0
        for row in matrix:
            if any([item != 0 for item in row]):
                break
            num_head_rows_delete += 1

        num_tail_rows_delete = 0
        for row in matrix[::-1]:  # trim from bottom row upwards
            if any([item != 0 for item in row]):
                break
            num_tail_rows_delete += 1  # if row was all zeros, mark it for deletions
        n_total_rows = len(matrix)
        matrix = matrix[num_head_rows_delete : n_total_rows - num_tail_rows_delete]
    else:
        num_head_rows_delete = 0

    if is_unicode_standard_output() and not force_ascii:
        block_chars = [" ", "▁", "▂", "▃", "▄", "▅", "▆", "▇", "█"]
        left_seven_eighths = "▉"
    else:
        block_chars = [" ", "*", "*", "*", "*", "*", "*", "*", "*"]
        left_seven_eighths = "*"

    # print text matrix
    out = []
    for row in np.flipud(matrix.T):
        # converts row into block chars
        c = [block_chars[item] for item in row]

        # add grid lines
        for i in xgrid:
            pos = (i - num_head_rows_delete) * bar_width - 1
            if row[pos] == 8 and (pos + 1 == len(row) or row[pos + 1] > 0):
                c[pos] = left_seven_eighths

        out.append("".join(c))

    return out
