# -*- coding: utf-8 -*-
#
from __future__ import division, print_function, unicode_literals

import sys


def hist(
    counts,
    bin_edges,
    orientation="vertical",
    max_width=40,
    bins=20,
    grid=None,
    bar_width=1,
    strip=False,
    force_ascii=False,
):
    if orientation == "vertical":
        return hist_vertical(
            counts,
            xgrid=grid,
            bar_width=bar_width,
            strip=strip,
            force_ascii=force_ascii,
        )

    assert orientation == "horizontal", "Unknown orientation '{}'".format(orientation)
    return hist_horizontal(
        counts,
        bin_edges,
        max_width=40,
        bins=20,
        bar_width=bar_width,
        force_ascii=force_ascii,
    )


def _trim_trailing_zeros(lst):
    k = 0
    for item in lst[::-1]:
        if item != 0:
            break
        k += 1
    return lst[:-k] if k > 0 else lst


def hist_horizontal(
    counts,
    bin_edges,
    max_width=40,
    bins=20,
    bar_width=1,
    show_bin_edges=True,
    show_counts=True,
    force_ascii=False,
):
    matrix = _get_matrix_of_eighths(counts, max_width, bar_width)

    if sys.stdout.encoding in ["UTF-8", "UTF8"] and not force_ascii:
        chars = [" ", "▏", "▎", "▍", "▌", "▋", "▊", "▉", "█"]
    else:
        chars = [" ", "*", "*", "*", "*", "*", "*", "*", "*"]

    fmt = []
    if show_bin_edges:
        efmt = "{:+.2e}"
        fmt.append(efmt + " - " + efmt)
    if show_counts:
        cfmt = "{{:{}d}}".format(max([len(str(c)) for c in counts]))
        fmt.append("[" + cfmt + "]")
    fmt.append("{}")
    fmt = "  ".join(fmt)

    out = []
    for k, (counts, row) in enumerate(zip(counts, matrix)):
        data = []
        if show_bin_edges:
            data.append(bin_edges[k])
            data.append(bin_edges[k + 1])
        if show_counts:
            data.append(counts)

        # Cut off trailing zeros
        r = _trim_trailing_zeros(row)
        data.append("".join(chars[item] for item in r))
        out.append(fmt.format(*data))

    return out


def _flip(matrix):
    n = len(matrix[0])
    return [[row[-(i + 1)] for row in matrix] for i in range(n)]


def hist_vertical(
    counts,
    bins=30,
    max_height=10,
    bar_width=2,
    strip=False,
    xgrid=None,
    force_ascii=False,
):
    if xgrid is None:
        xgrid = []

    matrix = _get_matrix_of_eighths(counts, max_height, bar_width)

    if strip:
        # Cut off leading and trailing rows of 0
        k0 = 0
        for row in matrix:
            if any([item != 0 for item in row]):
                break
            k0 += 1

        k1 = 0
        for row in matrix[::-1]:
            if any([item != 0 for item in row]):
                break
            k1 += 1
        n = len(matrix)
        matrix = matrix[k0 : n - k1]
    else:
        k0 = 0

    if sys.stdout.encoding in ["UTF-8", "UTF8"] and not force_ascii:
        block_chars = [" ", "▁", "▂", "▃", "▄", "▅", "▆", "▇", "█"]
        left_seven_eighths = "▉"
    else:
        block_chars = [" ", "*", "*", "*", "*", "*", "*", "*", "*"]
        left_seven_eighths = "*"

    # print text matrix
    out = []
    for row in _flip(matrix):

        # Cut off trailing zeros
        r = _trim_trailing_zeros(row)

        c = [block_chars[item] for item in r]

        # add grid lines
        for i in xgrid:
            # print(row[xgrid])
            pos = (i - k0) * bar_width - 1
            if row[pos] == 8 and (pos + 1 == len(row) or row[pos + 1] > 0):
                c[pos] = left_seven_eighths

        out.append("".join(c))

    return out


def _get_matrix_of_eighths(counts, max_size, bar_width):
    max_count = max(counts)

    # translate to eighths of a textbox
    eighths = [int(round(count / max_count * max_size * 8)) for count in counts]

    # prepare matrix
    matrix = [[0] * max_size for _ in range(len(eighths))]
    for i, eighth in enumerate(eighths):
        num_full_blocks = eighth // 8
        remainder = eighth % 8
        for j in range(num_full_blocks):
            matrix[i][j] = 8
        if remainder > 0:
            matrix[i][num_full_blocks] = remainder

    # Account for bar width
    out = []
    for i in range(len(matrix)):
        for _ in range(bar_width):
            out.append(matrix[i])
    return out
