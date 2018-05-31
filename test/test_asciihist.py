# -*- coding: utf-8 -*-
#
import numpy

import asciihist


def test_horizontal():
    # numpy.random.seed(123)
    sample = numpy.random.normal(size=1000)
    counts, bin_edges = numpy.histogram(sample)
    asciihist.hist(counts, bin_edges, orientation='horizontal')
    return


def test_vertical():
    # numpy.random.seed(123)
    sample = numpy.random.normal(size=1000)
    counts, bin_edges = numpy.histogram(sample)
    # sample = numpy.random.rand(1000)
    asciihist.hist(counts, bin_edges, grid=[5, 8])
    return


if __name__ == '__main__':
    # test_horizontal()
    test_vertical()
