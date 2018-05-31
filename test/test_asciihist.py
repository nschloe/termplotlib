# -*- coding: utf-8 -*-
#
import numpy

import asciihist


def test_hist():
    # numpy.random.seed(123)
    sample = numpy.random.normal(size=1000)
    asciihist.hist(sample)
    return


def test_hist2():
    # numpy.random.seed(123)
    sample = numpy.random.normal(size=(1000, 2))
    asciihist.hist(sample)
    return


if __name__ == '__main__':
    test_asciihist()
