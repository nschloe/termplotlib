# -*- coding: utf-8 -*-
#
from collections.abc import Sequence

from .helpers import create_padding_tuple


def _create_alignment(alignment, num_columns):
    if len(alignment) == 1:
        alignment = num_columns * alignment
    assert len(alignment) == num_columns
    return alignment


def _get_border_chars(border_style, ascii_mode):
    if isinstance(border_style, tuple):
        assert len(border_style) == 2
    else:
        border_style = (border_style, border_style)

    # Take care of the regular border first, then the block separators.
    border, block_sep = border_style

    if border is None:
        border_chars = None
    elif isinstance(border_style, list):
        assert len(border) == 11
        border_chars = border
    else:
        if ascii_mode:
            border_chars = {
                "thin": ["-", "|", "+", "+", "+", "+", "+", "+", "+", "+", "+"],
                "rounded": ["-", "|", "/", "\\", "\\", "/", "+", "+", "+", "+", "+"],
                "thick": ["=", "I", "+", "+", "+", "+", "+", "+", "+", "+", "+"],
                "double": ["=", "H", "+", "+", "+", "+", "+", "+", "+", "+", "+"],
            }[border]
        else:
            border_chars = {
                "thin": ["─", "│", "┌", "┐", "└", "┘", "├", "┤", "┬", "┴", "┼"],
                "rounded": ["─", "│", "╭", "╮", "╰", "╯", "├", "┤", "┬", "┴", "┼"],
                "thick": ["━", "┃", "┏", "┓", "┗", "┛", "┣", "┫", "┳", "┻", "╋"],
                "double": ["═", "║", "╔", "╗", "╚", "╝", "╠", "╣", "╦", "╩", "╬"],
            }[border]

    # block separators
    if block_sep is None:
        block_chars = None
    elif border == block_sep:
        bc = border_chars
        block_chars = [bc[6], bc[0], bc[10], bc[7]]
    else:
        if ascii_mode:
            block_chars = {
                ("thin", "thin"): ["+", "-", "+", "+"],
                ("thin", "rounded"): ["+", "-", "+", "+"],
                ("thin", "thick"): ["+", "=", "+", "+"],
                ("thin", "double"): ["+", "=", "+", "+"],
                #
                ("rounded", "thin"): ["+", "-", "+", "+"],
                ("rounded", "rounded"): ["+", "-", "+", "+"],
                ("rounded", "thick"): ["+", "=", "+", "+"],
                ("rounded", "double"): ["+", "=", "+", "+"],
                #
                ("thick", "thin"): ["+", "-", "+", "+"],
                ("thick", "rounded"): ["+", "-", "+", "+"],
                ("thick", "thick"): ["+", "=", "+", "+"],
                ("thick", "double"): ["+", "=", "+", "+"],
                #
                ("double", "thin"): ["+", "-", "+", "+"],
                ("double", "rounded"): ["+", "-", "+", "+"],
                ("double", "thick"): ["+", "=", "+", "+"],
                ("double", "double"): ["+", "=", "+", "+"],
            }[(border, block_sep)]
        else:
            block_chars = {
                ("thin", "thin"): ["├", "─", "┼", "┤"],
                ("thin", "rounded"): ["├", "─", "┼", "┤"],
                ("thin", "thick"): ["┝", "━", "┿", "┥"],
                ("thin", "double"): ["╞", "═", "╪", "╡"],
                #
                ("rounded", "thin"): ["├", "─", "┼", "┤"],
                ("rounded", "rounded"): ["├", "─", "┼", "┤"],
                ("rounded", "thick"): ["┝", "━", "┿", "┥"],
                ("rounded", "double"): ["╞", "═", "╪", "╡"],
                #
                ("thick", "thin"): ["┠", "─", "╂", "┨"],
                ("thick", "rounded"): ["┠", "─", "╂", "┨"],
                ("thick", "thick"): ["┣", "━", "╋", "┫"],
                ("thick", "double"): ["┠", "═", "╂", "┨"],
                #
                ("double", "thin"): ["╟", "─", "╫", "╢"],
                ("double", "rounded"): ["╟", "─", "╫", "╢"],
                ("double", "thick"): ["╟", "━", "╫", "╢"],
                ("double", "double"): ["╠", "═", "╬", "╣"],
            }[(border, block_sep)]

    return border_chars, block_chars


def _get_column_widths(strings, num_columns):
    column_widths = num_columns * [0]
    for block in strings:
        for row in block:
            for j, item in enumerate(row):
                column_widths[j] = max(column_widths[j], len(item))
    return column_widths


def _align(strings, alignments, column_widths):
    for block in strings:
        for row in block:
            for k, (item, align, cw) in enumerate(zip(row, alignments, column_widths)):
                rest = cw - len(item)
                if rest <= 0:
                    row[k] = item[:cw]
                else:
                    if align == "l":
                        left = 0
                    elif align == "r":
                        left = rest
                    else:
                        assert align == "c"
                        left = rest // 2
                    right = rest - left
                    row[k] = " " * left + item + " " * right
    return strings


def _add_padding(strings, column_widths, padding):
    for block in strings:
        for row in block:
            for k, (item, cw) in enumerate(zip(row, column_widths)):
                cw += padding[1] + padding[3]
                s = []
                for _ in range(padding[0]):
                    s += [" " * cw]
                s += [" " * padding[3] + item + " " * padding[1]]
                for _ in range(padding[2]):
                    s += [" " * cw]
                row[k] = "\n".join(s)
    return strings


def _seq_but_not_str(obj):
    return isinstance(obj, Sequence) and not isinstance(obj, (str, bytes, bytearray))


def _get_depth(l):
    if _seq_but_not_str(l):
        return 1 + max(_get_depth(item) for item in l)
    return 0


def _hjoin_multiline(join_char, strings):
    """Horizontal join of multiline strings
    """
    cstrings = [string.split("\n") for string in strings]
    max_num_lines = max(len(item) for item in cstrings)
    pp = []
    for k in range(max_num_lines):
        p = [cstring[k] for cstring in cstrings]
        pp.append(join_char + join_char.join(p) + join_char)

    return "\n".join([p.rstrip() for p in pp])


def table(
    data,
    alignment="l",
    padding=(0, 1),
    border_style=("thin", "double"),
    ascii_mode=False,
):
    try:
        depth = len(data.shape)
    except AttributeError:
        depth = _get_depth(data)

    if depth == 1:
        data = [[data]]
    elif depth == 2:
        data = [data]
    else:
        assert depth == 3

    # Make sure the data is consistent
    num_columns = len(data[0][0])
    for block in data:
        for row in block:
            assert len(row) == num_columns

    padding = create_padding_tuple(padding)
    alignments = _create_alignment(alignment, num_columns)
    border_chars, block_sep_chars = _get_border_chars(border_style, ascii_mode)

    strings = [[["{}".format(item) for item in row] for row in block] for block in data]

    column_widths = _get_column_widths(strings, num_columns)
    column_widths_with_padding = [c + padding[1] + padding[3] for c in column_widths]

    # add spaces according to alignment
    strings = _align(strings, alignments, column_widths)

    # add spaces according to padding
    strings = _add_padding(strings, column_widths, padding)

    # Join `strings` from the innermost to the outermost index.
    join_char = border_chars[1] if border_chars else ""
    for block in strings:
        for k, row in enumerate(block):
            block[k] = _hjoin_multiline(join_char, row)

    if border_chars:
        bc = border_chars
        cwp = column_widths_with_padding
        intermediate_border_row = (
            "\n" + bc[6] + bc[10].join([s * bc[0] for s in cwp]) + bc[7] + "\n"
        )
    else:
        intermediate_border_row = "\n"

    for k, block in enumerate(strings):
        strings[k] = intermediate_border_row.join(block)

    # bs = _get_block_separator_chars(border_style, block_separator, ascii_mode)
    if block_sep_chars:
        bs = block_sep_chars
        block_sep_row = (
            "\n" + bs[0] + bs[2].join([s * bs[1] for s in cwp]) + bs[3] + "\n"
        )
    else:
        block_sep_row = "\n"

    strings = block_sep_row.join(strings)

    if border_chars:
        bc = border_chars
        first_border_row = bc[2] + bc[8].join([s * bc[0] for s in cwp]) + bc[3] + "\n"
        last_border_row = "\n" + bc[4] + bc[9].join([s * bc[0] for s in cwp]) + bc[5]
    else:
        first_border_row = ""
        last_border_row = ""
    out = first_border_row + strings + last_border_row

    return out.split("\n")
