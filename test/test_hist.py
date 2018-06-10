# -*- coding: utf-8 -*-
#
import numpy

import asciiplotlib as apl


def test_horizontal():
    numpy.random.seed(123)
    sample = numpy.random.normal(size=1000)
    counts, bin_edges = numpy.histogram(sample)
    fig = apl.figure()
    fig.hist(counts, bin_edges, orientation="horizontal")
    string = fig.get_string()

    assert (
        string
        == """-3.23e+00 - -2.55e+00  [  7]  █
-2.55e+00 - -1.87e+00  [ 27]  ███▊
-1.87e+00 - -1.19e+00  [ 95]  █████████████▎
-1.19e+00 - -5.10e-01  [183]  █████████████████████████▋
-5.10e-01 - +1.70e-01  [286]  ████████████████████████████████████████
+1.70e-01 - +8.51e-01  [202]  ████████████████████████████▎
+8.51e-01 - +1.53e+00  [142]  ███████████████████▉
+1.53e+00 - +2.21e+00  [ 49]  ██████▉
+2.21e+00 - +2.89e+00  [  7]  █
+2.89e+00 - +3.57e+00  [  2]  ▎"""
    )
    return


def test_vertical():
    numpy.random.seed(123)
    sample = numpy.random.normal(size=1000)
    counts, bin_edges = numpy.histogram(sample)
    # sample = numpy.random.rand(1000)
    fig = apl.figure()
    fig.hist(counts, bin_edges, grid=[5, 8])
    string = fig.get_string()

    assert (
        string
        == """    █
    █
    ▉▁
   ▃▉█
   █▉█
   █▉██
  ▃█▉██
  ██▉██
  ██▉██▆
▂███▉██▉▂▁"""
    )
    return


def test_vertical_strip():
    numpy.random.seed(20)
    sample = numpy.random.normal(size=10000)
    counts, bin_edges = numpy.histogram(sample)
    fig = apl.figure()
    fig.hist(counts, bin_edges, grid=[5, 8], strip=True)
    string = fig.get_string()

    print(string)

    assert (
        string
        == """   ▉▆
   ▉█
   ▉█
  ▁▉█
  █▉█
  █▉██
  █▉██
 ▁█▉██
 ██▉██▃
▃██▉██▉▂"""
    )
    return


if __name__ == "__main__":
    test_horizontal()
    # test_vertical()
