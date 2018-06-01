# -*- coding: utf-8 -*-
#
import numpy

import asciiplotlib as apl


def test_subplot():
    fig = apl.figure()
    fig.hist()
    s1 = fig.subplot([1, 1, 1])
    s1.print('Some text')
    # apl.print('No meaning')
    # apl.subplot([1, 2, 2])
    # apl.print('More')
    # apl.print('meaningless text')
    # fig.show()
    return


if __name__ == '__main__':
    test_subplot()
