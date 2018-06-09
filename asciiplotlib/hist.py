# -*- coding: utf-8 -*-
#
from __future__ import division, print_function

import numpy


def hist(
    counts,
    bin_edges,
    orientation="vertical",
    max_width=40,
    bins=20,
    grid=None,
    bar_width=1,
):
    if orientation == "vertical":
        return hist_vertical(counts, xgrid=grid, bar_width=bar_width)

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

    chars = [
        " ",
        "\u258f",
        "\u258e",
        "\u258d",
        "\u258c",
        "\u258b",
        "\u258a",
        "\u2589",
        "\u2588",
    ]

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
        data.append("".join(chars[item] for item in row))
        out.append(fmt.format(*data))

    return out


def hist_vertical(counts, bins=30, max_height=10, bar_width=2, xgrid=None):
    if xgrid is None:
        xgrid = []

    matrix = _get_matrix_of_eighths(counts, max_height, bar_width)

    block_chars = [
        " ",
        "\u2581",
        "\u2582",
        "\u2583",
        "\u2584",
        "\u2585",
        "\u2586",
        "\u2587",
        "\u2588",
    ]

    left_seven_eighths = "\u2589"

    # print text matrix
    out = []
    for row in numpy.flipud(matrix.T):
        c = [block_chars[item] for item in row]
        for i in xgrid:
            # print(row[xgrid])
            pos = i * bar_width - 1
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
