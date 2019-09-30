from .barh import _get_matrix_of_eighths, _trim_trailing_zeros, barh
from .helpers import is_unicode_standard_output


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
    if show_bin_edges:
        labels = [
            "{:+.2e} - {:+.2e}".format(bin_edges[k], bin_edges[k + 1])
            for k in range(len(bin_edges) - 1)
        ]
    else:
        labels = None

    out = barh(
        counts,
        labels=labels,
        max_width=max_width,
        bar_width=bar_width,
        show_vals=show_counts,
        force_ascii=force_ascii,
    )

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

    if is_unicode_standard_output() and not force_ascii:
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
