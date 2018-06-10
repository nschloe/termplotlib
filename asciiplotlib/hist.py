# -*- coding: utf-8 -*-
#
from __future__ import division, print_function, unicode_literals

import numpy


def hist(
    counts,
    bin_edges,
    orientation="vertical",
    max_width=40,
    bins=20,
    grid=None,
    bar_width=1,
    strip=False,
):
    if orientation == "vertical":
        return hist_vertical(counts, xgrid=grid, bar_width=bar_width, strip=strip)

    assert orientation == "horizontal", "Unknown orientation '{}'".format(orientation)
    return hist_horizontal(
        counts, bin_edges, max_width=40, bins=20, bar_width=bar_width
    )


def hist_horizontal(
    counts,
    bin_edges,
    max_width=40,
    bins=20,
    bar_width=1,
    show_bin_edges=True,
    show_counts=True,
):
    matrix = _get_matrix_of_eighths(counts, max_width, bar_width)

    chars = [" ", "▏", "▎", "▍", "▌", "▋", "▊", "▉", "█"]

    fmt = []
    if show_bin_edges:
        efmt = "{:+.2e}"
        fmt.append(efmt + " - " + efmt)
    if show_counts:
        cfmt = "{{:{}d}}".format(numpy.max([len(str(c)) for c in counts]))
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
        r = numpy.trim_zeros(row, trim="b")
        data.append("".join(chars[item] for item in r))
        out.append(fmt.format(*data))

    return out


def hist_vertical(counts, bins=30, max_height=10, bar_width=2, strip=False, xgrid=None):
    if xgrid is None:
        xgrid = []

    matrix = _get_matrix_of_eighths(counts, max_height, bar_width)

    if strip:
        # Cut off leading and trailing rows of 0
        k0 = 0
        for row in matrix:
            if numpy.any(row != 0):
                break
            k0 += 1

        k1 = 0
        for row in matrix[::-1]:
            if numpy.any(row != 0):
                break
            k1 += 1
        n = matrix.shape[0]
        matrix = matrix[k0 : n - k1]
    else:
        k0 = 0

    block_chars = [" ", "▁", "▂", "▃", "▄", "▅", "▆", "▇", "█"]

    left_seven_eighths = "▉"

    # print text matrix
    out = []
    for row in numpy.flipud(matrix.T):

        # Cut off trailing zeros
        r = numpy.trim_zeros(row, trim="b")

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
    max_count = numpy.max(counts)

    # translate to eighths of a textbox
    eighths = numpy.array(
        [int(round(count / max_count * max_size * 8)) for count in counts]
    )

    # prepare matrix
    matrix = numpy.zeros((len(eighths), max_size), dtype=int)
    for k, eighth in enumerate(eighths):
        num_full_blocks = eighth // 8
        remainder = eighth % 8
        matrix[k, :num_full_blocks] = 8
        if remainder > 0:
            matrix[k, num_full_blocks] = remainder

    # Account for bar width
    matrix = numpy.repeat(matrix, numpy.full(matrix.shape[0], bar_width), axis=0)
    return matrix
