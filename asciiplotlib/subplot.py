# -*- coding: utf-8 -*-
#
from .figure import Figure


def subplot_grid(*args, **kwargs):
    return SubplotGrid(*args, **kwargs)


class SubplotGrid(object):
    def __init__(
        self, layout, width=80, column_widths=None, border_style=" ", padding=(1, 2)
    ):
        assert (
            len(layout) == 2
        ), "layout must be an interable of length 2 (rows and columns)"

        self._border_style = border_style
        self._border_char = "x"

        # border_width = {" ": 1}[border_style]
        border_width = 1
        self._num_borders = layout[1] + 1

        self._width = width

        if column_widths is None:
            self._column_widths = [
                (self._width - self._num_borders * border_width) // layout[1] for _ in range(layout[1])
            ]
            for k in range((self._width - self._num_borders * border_width) % layout[1]):
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
        total_width = self._num_borders + sum(self._column_widths)
        string += [self._border_char * total_width]

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
                    if len(s) > self._column_widths[j]:
                        s = s[: self._column_widths[j]]
                    elif len(s) < self._column_widths[j]:
                        s += " " * (self._column_widths[j] - len(s))
                    p.append(s)

                string += [
                    self._border_char + self._border_char.join(p) + self._border_char
                ]
            string += [self._border_char * total_width]

        return "\n".join(string)

    def __getitem__(self, ij):
        i, j = ij
        return self._subfigures[i][j]
