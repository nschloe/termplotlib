import termplotlib as tpl


def _generate_content(*args, **kwargs):
    grid = tpl.subplot_grid((2, 3), *args, **kwargs)
    grid[0, 0].aprint("Some text")
    grid[0, 1].aprint("Some more text\nand more")
    grid[0, 2].aprint("Some more text\nand more\neven more")
    grid[1, 0].aprint("Some more text\nand more\neven more")
    grid[1, 1].aprint("Some more text\nand more")
    grid[1, 2].aprint("Some text")
    return grid


def test_subplot():
    grid = tpl.subplot_grid((1, 2), width=20)
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
    grid = tpl.subplot_grid((1, 2), border_style="x", width=20)
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
    grid = tpl.subplot_grid((1, 2), width=20, border_style="thick")
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
    grid = tpl.subplot_grid((1, 2), width=20, padding=2, border_style="double")
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
    grid = _generate_content(width=40)
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
    grid = _generate_content(width=40, border_style="ascii")
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
    grid = _generate_content(width=40, border_style="thin rounded")
    string = grid.get_string()

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
    grid = _generate_content(
        width=40, border_style=["-", "|", "-", "-", "-", "-", "|", "|", "T", "-", "X"]
    )
    string = grid.get_string()

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

    grid.show()
    return


def test_subplot_no_borders():
    grid = _generate_content(width=40, border_style=None)
    string = grid.get_string()

    ref = """
  Some tex    Some mor    Some mor
              and more    and more
                          even mor


  Some mor    Some mor    Some tex
  and more    and more
  even mor"""

    assert string == ref
    return


def test_subplot_column_widths():
    grid = _generate_content(column_widths=(30, 15, 20))
    string = grid.get_string()

    print(string)

    assert (
        string
        == """┌──────────────────────────────┬───────────────┬────────────────────┐
│                              │               │                    │
│  Some text                   │  Some more t  │  Some more text    │
│                              │  and more     │  and more          │
│                              │               │  even more         │
│                              │               │                    │
├──────────────────────────────┼───────────────┼────────────────────┤
│                              │               │                    │
│  Some more text              │  Some more t  │  Some text         │
│  and more                    │  and more     │                    │
│  even more                   │               │                    │
│                              │               │                    │
└──────────────────────────────┴───────────────┴────────────────────┘"""
    )
    return


if __name__ == "__main__":
    test_subplot_padding()
