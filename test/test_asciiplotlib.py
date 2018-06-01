# -*- coding: utf-8 -*-
#
import numpy

import asciiplotlib as apl


def test_horizontal():
    # numpy.random.seed(123)
    sample = numpy.random.normal(size=1000)
    counts, bin_edges = numpy.histogram(sample)
    apl.hist(counts, bin_edges, orientation='horizontal')
    return


def test_vertical():
    # numpy.random.seed(123)
    sample = numpy.random.normal(size=1000)
    counts, bin_edges = numpy.histogram(sample)
    # sample = numpy.random.rand(1000)
    apl.hist(counts, bin_edges, grid=[5, 8])
    return


if __name__ == '__main__':
    # test_horizontal()
    test_vertical()
