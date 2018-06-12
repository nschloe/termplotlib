# -*- coding: utf-8 -*-
#
from .helpers import create_padding_tuple


def _create_alignment(alignment, num_columns):
    if len(alignment) == 1:
        alignment = num_columns * alignment
    return alignment


def _get_border_chars(border_style, ascii_mode):
    if border_style is None:
        border_chars = None
    elif len(border_style) == 1:
        border_chars = 11 * [border_style]
    elif isinstance(border_style, list):
        assert len(border_style) == 11
        border_chars = border_style
    else:
        if ascii_mode:
            border_chars = {
                "thin": ["-", "|", "+", "+", "+", "+", "+", "+", "+", "+", "+"],
                "thin rounded": ["-", "|", "/", "\\", "\\", "/", "+", "+", "+", "+", "+"],
                "thick": ["=", "I", "+", "+", "+", "+", "+", "+", "+", "+", "+"],
                "double": ["=", "H", "+", "+", "+", "+", "+", "+", "+", "+", "+"],
            }[border_style]
        else:
            border_chars = {
                "thin": ["─", "│", "┌", "┐", "└", "┘", "├", "┤", "┬", "┴", "┼"],
                "thin rounded": ["─", "│", "╭", "╮", "╰", "╯", "├", "┤", "┬", "┴", "┼"],
                "thick": ["━", "┃", "┏", "┓", "┗", "┛", "┣", "┫", "┳", "┻", "╋"],
                "double": ["═", "║", "╔", "╗", "╚", "╝", "╠", "╣", "╦", "╩", "╬"],
            }[border_style]

    return border_chars


def _get_header_separator_chars(border_style, header_separator, ascii_mode):
    if ascii_mode:
        header_chars = {
            ("thin", "thin"): ["+", "-", "+", "+"],
            ("thin", "thin rounded"): ["+", "-", "+", "+"],
            ("thin", "thick"): ["+", "=", "+", "+"],
            ("thin", "double"): ["+", "=", "+", "+"],
            #
            ("thin rounded", "thin"): ["+", "-", "+", "+"],
            ("thin rounded", "thin rounded"): ["+", "-", "+", "+"],
            ("thin rounded", "thick"): ["+", "=", "+", "+"],
            ("thin rounded", "double"): ["+", "=", "+", "+"],
            #
            ("thick", "thin"): ["+", "-", "+", "+"],
            ("thick", "thin rounded"): ["+", "-", "+", "+"],
            ("thick", "thick"): ["+", "=", "+", "+"],
            ("thick", "double"): ["+", "=", "+", "+"],
            #
            ("double", "thin"): ["+", "-", "+", "+"],
            ("double", "thin rounded"): ["+", "-", "+", "+"],
            ("double", "thick"): ["+", "=", "+", "+"],
            ("double", "double"): ["+", "=", "+", "+"],
        }[(border_style, header_separator)]
    else:
        header_chars = {
            ("thin", "thin"): ["├", "─", "┼", "┤"],
            ("thin", "thin rounded"): ["├", "─", "┼", "┤"],
            ("thin", "thick"): ["┝", "━", "┿", "┥"],
            ("thin", "double"): ["╞", "═", "╪", "╡"],
            #
            ("thin rounded", "thin"): ["├", "─", "┼", "┤"],
            ("thin rounded", "thin rounded"): ["├", "─", "┼", "┤"],
            ("thin rounded", "thick"): ["┝", "━", "┿", "┥"],
            ("thin rounded", "double"): ["╞", "═", "╪", "╡"],
            #
            ("thick", "thin"): ["┠", "─", "╂", "┨"],
            ("thick", "thin rounded"): ["┠", "─", "╂", "┨"],
            ("thick", "thick"): ["┣", "━", "╋", "┫"],
            ("thick", "double"): ["┠", "═", "╂", "┨"],
            #
            ("double", "thin"): ["╟", "─", "╫", "╢"],
            ("double", "thin rounded"): ["╟", "─", "╫", "╢"],
            ("double", "thick"): ["╟", "━", "╫", "╢"],
            ("double", "double"): ["╠", "═", "╬", "╣"],
        }[(border_style, header_separator)]

    return header_chars


def _get_column_widths(strings, num_columns):
    column_widths = num_columns * [0]
    for row in strings:
        for j, item in enumerate(row):
            column_widths[j] = max(column_widths[j], len(item))
    return column_widths


def _align(strings, alignments, column_widths):
    for row in strings:
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
    for row in strings:
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


def table(
    data,
    alignment="l",
    padding=(0, 1),
    header=None,
    border_style="thin",
    header_separator="double",
    ascii_mode=False
):
    # Make sure the data is consistent
    num_columns = len(data[0])
    for row in data:
        assert len(row) == num_columns

    if header:
        assert len(header) == num_columns

    padding = create_padding_tuple(padding)
    alignments = _create_alignment(alignment, num_columns)
    border_chars = _get_border_chars(border_style, ascii_mode)

    strings = [["{}".format(item) for item in row] for row in data]

    if header:
        strings = [["{}".format(item) for item in header]] + strings

    column_widths = _get_column_widths(strings, num_columns)
    column_widths_with_padding = [c + padding[1] + padding[3] for c in column_widths]

    # add spaces according to alignment
    strings = _align(strings, alignments, column_widths)

    # add spaces according to padding
    strings = _add_padding(strings, column_widths, padding)

    # collect the table rows
    srows = []
    for row in strings:
        cstrings = [item.split("\n") for item in row]
        max_num_lines = max(len(item) for item in cstrings)
        pp = []
        for k in range(max_num_lines):
            p = [cstring[k] for cstring in cstrings]
            if border_chars:
                join_char = border_chars[1]
            else:
                join_char = ""
            pp.append(join_char + join_char.join(p) + join_char)
        srows.append("\n".join([p.rstrip() for p in pp]))

    # collect the table
    if border_chars:
        bc = border_chars
        cwp = column_widths_with_padding
        first_border_row = bc[2] + bc[8].join([s * bc[0] for s in cwp]) + bc[3]
        intermediate_border_row = bc[6] + bc[10].join([s * bc[0] for s in cwp]) + bc[7]
        last_border_row = bc[4] + bc[9].join([s * bc[0] for s in cwp]) + bc[5]

        out = [first_border_row]
        if header:
            hs = _get_header_separator_chars(border_style, header_separator, ascii_mode)
            header_sep_row = hs[0] + hs[2].join([s * hs[1] for s in cwp]) + hs[3]
            out += [srows[0], header_sep_row]
            for k in range(1, len(srows) - 1):
                out += [srows[k], intermediate_border_row]
        else:
            for k in range(len(srows) - 1):
                out += [srows[k], intermediate_border_row]

        out += [srows[-1]]
        out += [last_border_row]
    else:
        out = srows

    return [s.rstrip() for s in out]
