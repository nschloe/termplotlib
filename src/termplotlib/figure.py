from typing import Optional

from .barh import barh
from .helpers import create_padding_tuple
from .hist import hist
from .plot import plot


def figure(*args, **kwargs):
    return Figure(*args, **kwargs)


class Figure:
    def __init__(self, width: Optional[int] = None, padding: int = 0):
        self._content = []
        self._width = width
        self._subfigures = None
        self._padding = create_padding_tuple(padding)

    def __rich_console__(self, *args):
        yield self.get_string()

    def aprint(self, string):
        self._content.append(string.split("\n"))

    def show(self):
        print(self.get_string())

    def get_string(self, remove_trailing_whitespace=True):
        lines = []

        padding_lr = self._padding[1] + self._padding[3]

        if self._width is None:
            line_lengths = [len(line) for c in self._content for line in c]
            width = max(line_lengths) if line_lengths else 0
            width += padding_lr
        else:
            width = self._width

        # Top padding
        lines += self._padding[0] * [" " * width]

        pr = " " * self._padding[1]
        pl = " " * self._padding[3]
        lines += [
            pl + line[: width - padding_lr] + pr for c in self._content for line in c
        ]

        # Bottom padding
        lines += self._padding[2] * [" " * width]

        if remove_trailing_whitespace:
            lines = [line.rstrip() for line in lines]

        return "\n".join(lines)

    def hist(self, *args, **kwargs):
        self._content.append(hist(*args, **kwargs))

    def barh(self, *args, **kwargs):
        self._content.append(barh(*args, **kwargs))

    def plot(self, *args, **kwargs):
        self._content.append(plot(*args, **kwargs))
