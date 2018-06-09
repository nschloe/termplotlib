# -*- coding: utf-8 -*-
#
from .hist import hist


def figure(*args, **kwargs):
    return Figure(*args, **kwargs)


class Figure(object):
    def __init__(self, width=80):
        self._content = []
        self._width = width
        self._subfigures = None
        return

    def aprint(self, string):
        self._content.append(string.split("\n"))
        return

    def show(self):
        print(self.get_string())
        return

    def get_string(self):
        return "\n".join([
            line[:self._width]
            for c in self._content
            for line in c
        ])

    def hist(self, *args, **kwargs):
        self._content.append(hist(*args, **kwargs))
        return
