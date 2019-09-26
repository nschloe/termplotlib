import sys

import numpy
import pytest

import termplotlib as tpl


@pytest.mark.skipif(
    sys.stdout.encoding not in ["UTF-8", "UTF8"],
    reason="Need UTF-8 terminal (not {})".format(sys.stdout.encoding),
)
def test_horizontal():
    numpy.random.seed(123)
    sample = numpy.random.normal(size=1000)
    counts, bin_edges = numpy.histogram(sample)
    fig = tpl.figure()
    fig.hist(counts, bin_edges, orientation="horizontal")
    # fig.show()
    string = fig.get_string()

    assert (
        string
        == """\
-3.23e+00 - -2.55e+00  [  7]  █
-2.55e+00 - -1.87e+00  [ 27]  ███▊
-1.87e+00 - -1.19e+00  [ 95]  █████████████▎
-1.19e+00 - -5.10e-01  [183]  █████████████████████████▋
-5.10e-01 - +1.70e-01  [286]  ████████████████████████████████████████
+1.70e-01 - +8.51e-01  [202]  ████████████████████████████▎
+8.51e-01 - +1.53e+00  [142]  ███████████████████▉
+1.53e+00 - +2.21e+00  [ 49]  ██████▉
+2.21e+00 - +2.89e+00  [  7]  █
+2.89e+00 - +3.57e+00  [  2]  ▎\
"""
    )
    return


def test_horizontal_ascii():
    numpy.random.seed(123)
    sample = numpy.random.normal(size=1000)
    counts, bin_edges = numpy.histogram(sample)
    fig = tpl.figure()
    fig.hist(counts, bin_edges, orientation="horizontal", force_ascii=True)
    string = fig.get_string()

    assert (
        string
        == """\
-3.23e+00 - -2.55e+00  [  7]  *
-2.55e+00 - -1.87e+00  [ 27]  ****
-1.87e+00 - -1.19e+00  [ 95]  **************
-1.19e+00 - -5.10e-01  [183]  **************************
-5.10e-01 - +1.70e-01  [286]  ****************************************
+1.70e-01 - +8.51e-01  [202]  *****************************
+8.51e-01 - +1.53e+00  [142]  ********************
+1.53e+00 - +2.21e+00  [ 49]  *******
+2.21e+00 - +2.89e+00  [  7]  *
+2.89e+00 - +3.57e+00  [  2]  *\
"""
    )
    return


@pytest.mark.skipif(
    sys.stdout.encoding not in ["UTF-8", "UTF8"],
    reason="Need UTF-8 terminal (not {})".format(sys.stdout.encoding),
)
def test_vertical():
    numpy.random.seed(123)
    sample = numpy.random.normal(size=1000)
    counts, bin_edges = numpy.histogram(sample, bins=40)
    fig = tpl.figure()
    fig.hist(counts, bin_edges)
    fig.show()

    string = fig.get_string()

    assert (
        string
        == """\
                  ▆█
                ▄▄██
               ▃█████
              ▁██████▃  ▅
            ▂ ████████▇▅█
           ▂█▅████████████
          ▂███████████████▃▂
        ▂▃██████████████████▃▁
      ▁▂██████████████████████
▂ ▃▂▄▄█████████████████████████▅▃▁▂▁▁  ▁\
"""
    )
    return


def test_vertical_ascii():
    numpy.random.seed(123)
    sample = numpy.random.normal(size=1000)
    counts, bin_edges = numpy.histogram(sample, bins=40)
    fig = tpl.figure()
    fig.hist(counts, bin_edges, force_ascii=True)
    # fig.show()

    string = fig.get_string()

    assert (
        string
        == """\
                  **
                ****
               ******
              ********  *
            * ***********
           ***************
          ******************
        **********************
      ************************
* ***********************************  *\
"""
    )
    return


@pytest.mark.skipif(
    sys.stdout.encoding not in ["UTF-8", "UTF8"],
    reason="Need UTF-8 terminal (not {})".format(sys.stdout.encoding),
)
def test_vertical_grid():
    numpy.random.seed(123)
    sample = numpy.random.normal(size=1000)
    counts, bin_edges = numpy.histogram(sample, bins=40)
    fig = tpl.figure()
    fig.hist(counts, bin_edges, grid=[15, 25])
    # fig.show()
    string = fig.get_string()

    assert (
        string
        == """\
                  ▆█
                ▄▄██
               ▃█████
              ▁██████▃  ▅
            ▂ ▉███████▇▅█
           ▂█▅▉█████████▉█
          ▂███▉█████████▉█▃▂
        ▂▃████▉█████████▉███▃▁
      ▁▂██████▉█████████▉█████
▂ ▃▂▄▄████████▉█████████▉██████▅▃▁▂▁▁  ▁\
"""
    )
    return


@pytest.mark.skipif(
    sys.stdout.encoding not in ["UTF-8", "UTF8"],
    reason="Need UTF-8 terminal (not {})".format(sys.stdout.encoding),
)
def test_vertical_strip():
    numpy.random.seed(20)
    sample = numpy.random.normal(size=10000)
    counts, bin_edges = numpy.histogram(sample)
    fig = tpl.figure()
    fig.hist(counts, bin_edges, grid=[5, 8], strip=True)
    string = fig.get_string()

    assert (
        string
        == """\
   ▉▆
   ▉█
   ▉█
  ▁▉█
  █▉█
  █▉██
  █▉██
 ▁█▉██
 ██▉██▃
▃██▉██▉▂\
"""
    )
    return


if __name__ == "__main__":
    # test_horizontal_ascii()
    test_vertical_grid()
