import sys

import numpy as np
import pytest

import termplotlib as tpl


@pytest.mark.skipif(
    sys.stdout.encoding.upper() not in ["UTF-8", "UTF8"],
    reason=f"Need UTF-8 terminal (not {sys.stdout.encoding})",
)
def test_horizontal():
    rng = np.random.default_rng(123)
    sample = rng.standard_normal(size=1000)
    counts, bin_edges = np.histogram(sample)
    fig = tpl.figure()
    fig.hist(counts, bin_edges, orientation="horizontal")
    # fig.show()
    string = fig.get_string()

    ref = """\
-3.30e+00 - -2.66e+00  [  8]  █▎
-2.66e+00 - -2.03e+00  [ 22]  ███▌
-2.03e+00 - -1.39e+00  [ 50]  ████████
-1.39e+00 - -7.56e-01  [123]  ███████████████████▋
-7.56e-01 - -1.20e-01  [236]  █████████████████████████████████████▊
-1.20e-01 - +5.16e-01  [250]  ████████████████████████████████████████
+5.16e-01 - +1.15e+00  [172]  ███████████████████████████▌
+1.15e+00 - +1.79e+00  [111]  █████████████████▊
+1.79e+00 - +2.42e+00  [ 22]  ███▌
+2.42e+00 - +3.06e+00  [  6]  █\
"""

    assert string == ref, string


def test_horizontal_ascii():
    rng = np.random.default_rng(123)
    sample = rng.standard_normal(size=1000)
    counts, bin_edges = np.histogram(sample)
    fig = tpl.figure()
    fig.hist(counts, bin_edges, orientation="horizontal", force_ascii=True)
    string = fig.get_string()

    ref = """\
-3.30e+00 - -2.66e+00  [  8]  **
-2.66e+00 - -2.03e+00  [ 22]  ****
-2.03e+00 - -1.39e+00  [ 50]  ********
-1.39e+00 - -7.56e-01  [123]  ********************
-7.56e-01 - -1.20e-01  [236]  **************************************
-1.20e-01 - +5.16e-01  [250]  ****************************************
+5.16e-01 - +1.15e+00  [172]  ****************************
+1.15e+00 - +1.79e+00  [111]  ******************
+1.79e+00 - +2.42e+00  [ 22]  ****
+2.42e+00 - +3.06e+00  [  6]  *\
"""

    assert string == ref, string


@pytest.mark.skipif(
    sys.stdout.encoding.upper() not in ["UTF-8", "UTF8"],
    reason=f"Need UTF-8 terminal (not {sys.stdout.encoding})",
)
def test_vertical():
    rng = np.random.default_rng(123)
    sample = rng.standard_normal(size=1000)
    counts, bin_edges = np.histogram(sample, bins=40)
    fig = tpl.figure()
    fig.hist(counts, bin_edges)
    fig.show()

    string = fig.get_string()

    ref = """\
                  ▇  █
                ▁ █ ▁█ ▄
                █ █▂██▁█
                █▅██████ ▄▄
               ▃████████▃██ ▆
               ████████████▇█
            ▅▅▇██████████████▁▅
           ▂███████████████████▃
      ▃▁ ▅▇█████████████████████
▂ ▂▄ ▄███████████████████████████▆▄▅▃▂ ▁\
"""

    assert string == ref, "\n" + string


def test_vertical_ascii():
    rng = np.random.default_rng(123)
    sample = rng.standard_normal(size=1000)
    counts, bin_edges = np.histogram(sample, bins=40)
    fig = tpl.figure()
    fig.hist(counts, bin_edges, force_ascii=True)
    # fig.show()

    string = fig.get_string()

    ref = """\
                  *  *
                * * ** *
                * ******
                ******** **
               ************ *
               **************
            *******************
           *********************
      ** ***********************
* ** ********************************* *"""

    assert string == ref, "\n" + string


@pytest.mark.skipif(
    sys.stdout.encoding.upper() not in ["UTF-8", "UTF8"],
    reason=f"Need UTF-8 terminal (not {sys.stdout.encoding})",
)
def test_vertical_grid():
    rng = np.random.default_rng(123)
    sample = rng.standard_normal(size=1000)
    counts, bin_edges = np.histogram(sample, bins=40)
    fig = tpl.figure()
    fig.hist(counts, bin_edges, grid=[15, 25])
    # fig.show()
    string = fig.get_string()

    ref = """\
                  ▇  █
                ▁ █ ▁█ ▄
                █ █▂██▁█
                █▅██████ ▄▄
               ▃████████▃██ ▆
               █████████▉██▇█
            ▅▅▇█████████▉████▁▅
           ▂██▉█████████▉██████▃
      ▃▁ ▅▇███▉█████████▉███████
▂ ▂▄ ▄████████▉█████████▉████████▆▄▅▃▂ ▁"""

    assert string == ref, "\n" + string


@pytest.mark.skipif(
    sys.stdout.encoding.upper() not in ["UTF-8", "UTF8"],
    reason=f"Need UTF-8 terminal (not {sys.stdout.encoding})",
)
def test_vertical_strip():
    rng = np.random.default_rng(20)
    sample = rng.standard_normal(size=10000)
    counts, bin_edges = np.histogram(sample)
    fig = tpl.figure()
    fig.hist(counts, bin_edges, grid=[5, 8], strip=True)
    string = fig.get_string()

    ref = """\
    ▂█
    ▉█
    ▉█
    ▉█▃
   ▃▉██
   █▉██
   █▉██
   █▉██▆
  ██▉███
▁▄██▉██▉▆▁"""

    assert string == ref, "\n" + string


if __name__ == "__main__":
    # test_horizontal_ascii()
    test_vertical_grid()
