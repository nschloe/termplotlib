# -*- coding: utf-8 -*-
#
import asciiplotlib as apl


def test_subplot():
    grid = apl.subplot_grid((1, 2), width=20)
    grid[0, 0].aprint("Some text")
    grid[0, 1].aprint("Some more text")
    string = grid.get_string()
    assert (
        string
        == """┌─────────┬────────┐
│         │        │
│  Some   │  Some  │
│         │        │
└─────────┴────────┘"""
    )
    return


def test_subplot_custom_border():
    grid = apl.subplot_grid((1, 2), border_style="x", width=20)
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
    grid = apl.subplot_grid((1, 2), width=20, border_style="thick")
    grid[0, 0].aprint("Some text")
    grid[0, 1].aprint("Some more text\nand more")
    string = grid.get_string()
    assert (
        string
        == """┏━━━━━━━━━┳━━━━━━━━┓
┃         ┃        ┃
┃  Some   ┃  Some  ┃
┃         ┃  and   ┃
┃         ┃        ┃
┗━━━━━━━━━┻━━━━━━━━┛"""
    )
    return


def test_subplot_padding():
    grid = apl.subplot_grid((1, 2), width=20, padding=2, border_style="double")
    grid[0, 0].aprint("Some text")
    grid[0, 1].aprint("Some more text\nand more")
    string = grid.get_string()
    assert (
        string
        == """╔═════════╦════════╗
║         ║        ║
║         ║        ║
║  Some   ║  Some  ║
║         ║  and   ║
║         ║        ║
║         ║        ║
╚═════════╩════════╝"""
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
        == """┌────────────┬────────────┬────────────┐
│            │            │            │
│  Some tex  │  Some mor  │  Some mor  │
│            │  and more  │  and more  │
│            │            │  even mor  │
│            │            │            │
├────────────┼────────────┼────────────┤
│            │            │            │
│  Some mor  │  Some mor  │  Some tex  │
│  and more  │  and more  │            │
│  even mor  │            │            │
│            │            │            │
└────────────┴────────────┴────────────┘"""
    )
    return


def test_subplot_ascii():
    grid = apl.subplot_grid((2, 3), width=40, border_style="ascii")
    grid[0, 0].aprint("Some text")
    grid[0, 1].aprint("Some more text\nand more")
    grid[0, 2].aprint("Some more text\nand more\neven more")
    grid[1, 0].aprint("Some more text\nand more\neven more")
    grid[1, 1].aprint("Some more text\nand more")
    grid[1, 2].aprint("Some text")
    string = grid.get_string()

    assert (
        string
        == """----------------------------------------
|            |            |            |
|  Some tex  |  Some mor  |  Some mor  |
|            |  and more  |  and more  |
|            |            |  even mor  |
|            |            |            |
|------------+------------+------------|
|            |            |            |
|  Some mor  |  Some mor  |  Some tex  |
|  and more  |  and more  |            |
|  even mor  |            |            |
|            |            |            |
----------------------------------------"""
    )
    return


def test_subplot_thin_rounded():
    grid = apl.subplot_grid((2, 3), width=40, border_style="thin rounded")
    grid[0, 0].aprint("Some text")
    grid[0, 1].aprint("Some more text\nand more")
    grid[0, 2].aprint("Some more text\nand more\neven more")
    grid[1, 0].aprint("Some more text\nand more\neven more")
    grid[1, 1].aprint("Some more text\nand more")
    grid[1, 2].aprint("Some text")
    string = grid.get_string()

    print(string)

    assert (
        string
        == """╭────────────┬────────────┬────────────╮
│            │            │            │
│  Some tex  │  Some mor  │  Some mor  │
│            │  and more  │  and more  │
│            │            │  even mor  │
│            │            │            │
├────────────┼────────────┼────────────┤
│            │            │            │
│  Some mor  │  Some mor  │  Some tex  │
│  and more  │  and more  │            │
│  even mor  │            │            │
│            │            │            │
╰────────────┴────────────┴────────────╯"""
    )
    return


def test_subplot_custom():
    grid = apl.subplot_grid(
        (2, 3),
        width=40,
        border_style=["-", "|", "-", "-", "-", "-", "|", "|", "T", "-", "X"],
    )
    grid[0, 0].aprint("Some text")
    grid[0, 1].aprint("Some more text\nand more")
    grid[0, 2].aprint("Some more text\nand more\neven more")
    grid[1, 0].aprint("Some more text\nand more\neven more")
    grid[1, 1].aprint("Some more text\nand more")
    grid[1, 2].aprint("Some text")
    string = grid.get_string()

    print(string)

    assert (
        string
        == """-------------T------------T-------------
|            |            |            |
|  Some tex  |  Some mor  |  Some mor  |
|            |  and more  |  and more  |
|            |            |  even mor  |
|            |            |            |
|------------X------------X------------|
|            |            |            |
|  Some mor  |  Some mor  |  Some tex  |
|  and more  |  and more  |            |
|  even mor  |            |            |
|            |            |            |
----------------------------------------"""
    )
    return


if __name__ == "__main__":
    test_subplot_padding()
