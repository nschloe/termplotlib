# -*- coding: utf-8 -*-
#
import asciiplotlib as apl


def test_subplot():
    grid = apl.subplot_grid((1, 2), border_style="|", width=20)
    grid[0, 0].aprint("Some text")
    grid[0, 1].aprint("Some more text")
    string = grid.get_string()
    assert string == '''xxxxxxxxxxxxxxxxxxxx
x         x        x
x  Some   x  Some  x
x         x        x
xxxxxxxxxxxxxxxxxxxx'''
    return


def test_subplot2():
    grid = apl.subplot_grid((1, 2), width=20)
    grid[0, 0].aprint("Some text")
    grid[0, 1].aprint("Some more text\nand more")
    string = grid.get_string()
    assert string == '''xxxxxxxxxxxxxxxxxxxx
x         x        x
x  Some   x  Some  x
x         x  and   x
x         x        x
xxxxxxxxxxxxxxxxxxxx'''
    return


def test_subplot_padding():
    grid = apl.subplot_grid((1, 2), width=20, padding=2)
    grid[0, 0].aprint("Some text")
    grid[0, 1].aprint("Some more text\nand more")
    string = grid.get_string()
    assert string == '''xxxxxxxxxxxxxxxxxxxx
x         x        x
x         x        x
x  Some   x  Some  x
x         x  and   x
x         x        x
x         x        x
xxxxxxxxxxxxxxxxxxxx'''
    return


if __name__ == '__main__':
    test_subplot_padding()
