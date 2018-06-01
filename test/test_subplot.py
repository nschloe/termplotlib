# -*- coding: utf-8 -*-
#
import numpy

import asciiplotlib as apl


def test_subplot():
    apl.subplot([1, 1, 1])
    apl.raw(
        'Some text \n'
        'No meaning'
        )
    apl.subplot([1, 2, 2])
    apl.raw(
        'More \n'
        'meaningless text'
        )
    apl.show()
    return


if __name__ == '__main__':
    test_subplot()
