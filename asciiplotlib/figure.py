# -*- coding: utf-8 -*-
#
from .hist import hist
from .plot import plot


def figure(*args, **kwargs):
    return Figure(*args, **kwargs)


class Figure(object):
    def __init__(self, width=80, padding=0):
        self._content = []
        self._width = width
        self._subfigures = None

        # self._padding is a 4-tuple: top, right, bottom, left (just like CSS)
        if isinstance(padding, int):
            self._padding = (padding, padding, padding, padding)
        else:
            if len(padding) == 1:
                self._padding = (padding[0], padding[0], padding[0], padding[0])
            elif len(padding) == 2:
                self._padding = (padding[0], padding[1], padding[0], padding[1])
            elif len(padding) == 3:
                self._padding = (padding[0], padding[1], padding[2], padding[1])
            else:
                assert len(padding) == 4
                self._padding = (padding[0], padding[1], padding[2], padding[3])
        return

    def aprint(self, string):
        self._content.append(string.split("\n"))
        return

    def show(self):
        print(self.get_string())
        return

    def get_string(self):
        lines = []

        # Top padding
        lines += self._padding[0] * [" " * self._width]

        padding_lr = self._padding[1] + self._padding[3]
        pr = " " * self._padding[1]
        pl = " " * self._padding[3]
        lines += [
            pl + line[: self._width - padding_lr] + pr
            for c in self._content
            for line in c
        ]

        # Bottom padding
        lines += self._padding[2] * [" " * self._width]
        return "\n".join([line.rstrip() for line in lines])

    def hist(self, *args, **kwargs):
        self._content.append(hist(*args, **kwargs))
        return

    def plot(self, *args, **kwargs):
        self._content.append(plot(*args, **kwargs))
        return
