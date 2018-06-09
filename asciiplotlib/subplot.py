# -*- coding: utf-8 -*-
#
from .figure import Figure


def subplot_grid(*args, **kwargs):
    return SubplotGrid(*args, **kwargs)


class SubplotGrid(object):
    def __init__(
        self, layout, width=80, column_widths=None, border_style=" ", padding=1
    ):
        assert (
            len(layout) == 2
        ), "layout must be an interable of length 2 (rows and columns)"

        self._border_style = border_style
        self._border_char = "x"

        self._padding = padding

        # border_width = {" ": 1}[border_style]
        border_width = 1

        self._width = width

        if column_widths is None:
            self._column_widths = [
                (self._width - 3 * border_width) // layout[1] for _ in range(layout[1])
            ]
            for k in range((self._width - 3 * border_width) % layout[1]):
                self._column_widths[k] += 1
        else:
            assert len(column_widths) == layout[1]
            self._columns_widths = column_widths

        self._subfigures = [
            [Figure(self._column_widths[j]) for j in range(layout[1])]
            for _ in range(layout[0])
        ]
        return

    def show(self):
        print(self.get_string())
        return

    def get_string(self):
        string = []
        total_width = 3 + sum(self._column_widths)
        string += [self._border_char * total_width]

        vertical_padding = (
            self._border_char
            + self._border_char.join([k * " " for k in self._column_widths])
            + self._border_char
        )

        string += self._padding * [vertical_padding]

        for row in self._subfigures:
            cstrings = [item.get_string().split("\n") for item in row]
            max_num_lines = max(len(item) for item in cstrings)
            for k in range(max_num_lines):
                p = []
                for j, cstring in enumerate(cstrings):
                    try:
                        s = cstring[k]
                    except IndexError:
                        s = ""
                    if len(s) > self._column_widths[j] - 2 * self._padding:
                        s = s[: self._column_widths[j] - 2 * self._padding]
                    elif len(s) < self._column_widths[j] - 2 * self._padding:
                        s += " " * (self._column_widths[j] - 2 * self._padding - len(s))
                    p.append(s)

                pd = " " * self._padding
                string += [
                    self._border_char
                    + pd
                    + (pd + self._border_char + pd).join(p)
                    + pd
                    + self._border_char
                ]

        string += self._padding * [vertical_padding]
        string += [self._border_char * total_width]

        return "\n".join(string)

    def __getitem__(self, ij):
        i, j = ij
        return self._subfigures[i][j]
