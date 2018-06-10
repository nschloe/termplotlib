# -*- coding: utf-8 -*-
#
import asciiplotlib as apl


def test_subplot():
    grid = apl.subplot_grid((1, 2), border_style="|", width=20)
    grid[0, 0].aprint("Some text")
    grid[0, 1].aprint("Some more text")
    string = grid.get_string()
    assert (
        string
        == """xxxxxxxxxxxxxxxxxxxx
x         x        x
x  Some   x  Some  x
x         x        x
xxxxxxxxxxxxxxxxxxxx"""
    )
    return


def test_subplot2():
    grid = apl.subplot_grid((1, 2), width=20)
    grid[0, 0].aprint("Some text")
    grid[0, 1].aprint("Some more text\nand more")
    string = grid.get_string()
    assert (
        string
        == """xxxxxxxxxxxxxxxxxxxx
x         x        x
x  Some   x  Some  x
x         x  and   x
x         x        x
xxxxxxxxxxxxxxxxxxxx"""
    )
    return


def test_subplot_padding():
    grid = apl.subplot_grid((1, 2), width=20, padding=2)
    grid[0, 0].aprint("Some text")
    grid[0, 1].aprint("Some more text\nand more")
    string = grid.get_string()
    assert (
        string
        == """xxxxxxxxxxxxxxxxxxxx
x         x        x
x         x        x
x  Some   x  Some  x
x         x  and   x
x         x        x
x         x        x
xxxxxxxxxxxxxxxxxxxx"""
    )
    return


def test_subplot_3x2():
    grid = apl.subplot_grid((2, 3), width=40)
    grid[0, 0].aprint("Some text")
    grid[0, 1].aprint("Some more text\nand more")
    grid[0, 2].aprint("Some more text\nand more\neven more")
    grid[1, 0].aprint("Some more text\nand more\neven more")
    grid[1, 1].aprint("Some more text\nand more")
    grid[1, 2].aprint("Some text")
    string = grid.get_string()
    assert (
        string
        == """xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
x            x            x            x
x  Some tex  x  Some mor  x  Some mor  x
x            x  and more  x  and more  x
x            x            x  even mor  x
x            x            x            x
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
x            x            x            x
x  Some mor  x  Some mor  x  Some tex  x
x  and more  x  and more  x            x
x  even mor  x            x            x
x            x            x            x
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"""
    )
    return


if __name__ == "__main__":
    test_subplot_padding()
