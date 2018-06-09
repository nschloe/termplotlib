# -*- coding: utf-8 -*-
#
import asciiplotlib as apl


def test_subplot():
    grid = apl.subplot_grid((1, 2), border_style="|")
    grid[0, 0].aprint("Some text")
    grid[0, 1].aprint("Some more text")
    grid.show()
    # fig = apl.figure()
    # fig.hist()
    # s1 = fig.subplot([1, 1, 1])
    # s1.print('Some text')
    # apl.print('No meaning')
    # apl.subplot([1, 2, 2])
    # apl.print('More')
    # apl.print('meaningless text')
    # fig.show()
    return


if __name__ == '__main__':
    test_subplot()
