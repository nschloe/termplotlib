from typing import List, Optional, Tuple, Union

from .figure import Figure


def subplot_grid(*args, **kwargs):
    return SubplotGrid(*args, **kwargs)


class SubplotGrid:
    def __init__(
        self,
        layout,
        width: Optional[int] = None,
        column_widths: Optional[List[int]] = None,
        border_style: str = "thin",
        padding: Union[int, List[int], Tuple[int, int]] = (1, 2),
    ):
        assert (
            len(layout) == 2
        ), "layout must be an interable of length 2 (rows and columns)"

        self._layout = layout

        if border_style is None:
            self._border_chars = None
        elif len(border_style) == 1:
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

        if column_widths is None:
            if width is None:
                self._column_widths = [None] * layout[1]
            else:
                self._column_widths = [
                    (width - self._num_borders * border_width) // layout[1]
                    for _ in range(layout[1])
                ]
                for k in range((width - self._num_borders * border_width) % layout[1]):
                    self._column_widths[k] += 1
        else:
            assert (
                width is None
            ), "At most one of `width` and `column_widths` can be specified."
            assert len(column_widths) == layout[1]
            self._column_widths = column_widths

        self._subfigures = [
            [Figure(self._column_widths[j], padding=padding) for j in range(layout[1])]
            for _ in range(layout[0])
        ]

    def show(self):
        print(self.get_string())

    def get_string(self):
        # compute column width
        cstrings = [
            [item.get_string(remove_trailing_whitespace=False) for item in row]
            for row in self._subfigures
        ]
        column_widths = [
            max(
                len(line)
                for i in range(self._layout[0])
                for line in cstrings[i][j].split("\n")
            )
            for j in range(self._layout[1])
        ]

        string = []

        if self._border_chars:
            string += [
                self._border_chars[2]
                + self._border_chars[8].join(
                    [s * self._border_chars[0] for s in column_widths]
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
                    # truncate or extend with spaces to match the column width
                    if len(s) >= column_widths[j]:
                        s = s[: column_widths[j]]
                    else:
                        s += " " * (column_widths[j] - len(s))
                    p.append(s)
                if self._border_chars:
                    join_char = self._border_chars[1]
                else:
                    join_char = ""
                pp.append(join_char + join_char.join(p) + join_char)
            srows.append("\n".join([p.rstrip() for p in pp]))

        if self._border_chars:
            intermediate_border_row = (
                "\n"
                + self._border_chars[6]
                + self._border_chars[10].join(
                    [s * self._border_chars[0] for s in column_widths]
                )
                + self._border_chars[7]
                + "\n"
            )
        else:
            intermediate_border_row = "\n"
        string += [intermediate_border_row.join(srows)]

        if self._border_chars:
            # final row
            string += [
                self._border_chars[4]
                + self._border_chars[9].join(
                    [s * self._border_chars[0] for s in column_widths]
                )
                + self._border_chars[5]
            ]

        return "\n".join([s.rstrip() for s in string])

    def __getitem__(self, ij):
        i, j = ij
        if i >= self._layout[0]:
            raise IndexError(
                f"Row index too large! (idx {i}, only {self._layout[0]} rows)"
            )
        if j >= self._layout[1]:
            raise IndexError(
                f"Col index too large! (idx {j}, only {self._layout[1]} cols)"
            )
        return self._subfigures[i][j]
