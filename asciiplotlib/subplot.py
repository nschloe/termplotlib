# -*- coding: utf-8 -*-
#
from __future__ import unicode_literals

from .figure import Figure


def subplot_grid(*args, **kwargs):
    return SubplotGrid(*args, **kwargs)


class SubplotGrid(object):
    def __init__(
        self, layout, width=80, column_widths=None, border_style="thin", padding=(1, 2)
    ):
        assert (
            len(layout) == 2
        ), "layout must be an interable of length 2 (rows and columns)"

        if len(border_style) == 1:
            self._border_chars = 11 * [border_style]
        elif isinstance(border_style, list):
            assert len(border_style) == 11
            self._border_chars = border_style
        else:
            self._border_chars = {
                "thin": ["─", "│", "┌", "┐", "└", "┘", "├", "┤", "┬", "┴", "┼"],
                "thin rounded": ["─", "│", "╭", "╮", "╰", "╯", "├", "┤", "┬", "┴", "┼"],
                "thick": ["━", "┃", "┏", "┓", "┗", "┛", "┣", "┫", "┳", "┻", "╋"],
                "double": ["═", "║", "╔", "╗", "╚", "╝", "╠", "╣", "╦", "╩", "╬"],
                "ascii": ["-", "|", "-", "-", "-", "-", "|", "|", "-", "-", "+"],
            }[border_style]

        border_width = 1
        self._num_borders = layout[1] + 1

        self._width = width

        if column_widths is None:
            self._column_widths = [
                (self._width - self._num_borders * border_width) // layout[1]
                for _ in range(layout[1])
            ]
            for k in range(
                (self._width - self._num_borders * border_width) % layout[1]
            ):
                self._column_widths[k] += 1
        else:
            assert len(column_widths) == layout[1]
            self._columns_widths = column_widths

        self._subfigures = [
            [Figure(self._column_widths[j], padding=padding) for j in range(layout[1])]
            for _ in range(layout[0])
        ]
        return

    def show(self):
        print(self.get_string())
        return

    def get_string(self):
        string = []

        string += [
            self._border_chars[2]
            + self._border_chars[8].join(
                [s * self._border_chars[0] for s in self._column_widths]
            )
            + self._border_chars[3]
        ]

        # collect the subfigure rows
        srows = []
        for row in self._subfigures:
            cstrings = [item.get_string().split("\n") for item in row]
            max_num_lines = max(len(item) for item in cstrings)
            pp = []
            for k in range(max_num_lines):
                p = []
                for j, cstring in enumerate(cstrings):
                    try:
                        s = cstring[k]
                    except IndexError:
                        s = ""
                    # truncate or extend with spaces to match teh column width
                    if len(s) >= self._column_widths[j]:
                        s = s[: self._column_widths[j]]
                    else:
                        s += " " * (self._column_widths[j] - len(s))
                    p.append(s)
                pp.append(
                    self._border_chars[1]
                    + self._border_chars[1].join(p)
                    + self._border_chars[1]
                )
            srows.append("\n".join(pp))

        intermediate_border_row = (
            "\n"
            + self._border_chars[6]
            + self._border_chars[10].join(
                [s * self._border_chars[0] for s in self._column_widths]
            )
            + self._border_chars[7]
            + "\n"
        )
        string += [intermediate_border_row.join(srows)]

        # final row
        string += [
            self._border_chars[4]
            + self._border_chars[9].join(
                [s * self._border_chars[0] for s in self._column_widths]
            )
            + self._border_chars[5]
        ]

        return "\n".join(string)

    def __getitem__(self, ij):
        i, j = ij
        return self._subfigures[i][j]
