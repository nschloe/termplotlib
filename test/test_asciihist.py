# -*- coding: utf-8 -*-
#
import numpy

import asciihist


def test_horizontal():
    # numpy.random.seed(123)
    sample = numpy.random.normal(size=1000)
    asciihist.hist(sample, orientation='horizontal')
    return


def test_vertical():
    # numpy.random.seed(123)
    sample = numpy.random.normal(size=1000)
    asciihist.hist(sample)
    return


if __name__ == '__main__':
    test_horizontal()
