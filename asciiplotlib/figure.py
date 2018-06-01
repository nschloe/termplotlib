# -*- coding: utf-8 -*-
#
from .hist import hist


def figure():
    return Figure()


class Figure(object):
    def __init__(self):
        self._content = []
        return

    def subplot(self):
        return

    def aprint(self):
        return

    def show(self):
        for c in self._content:
            for line in c:
                print(line)
        return

    def hist(self, *args, **kwargs):
        self._content.append(hist(*args, **kwargs))
        return
