import numpy as np

import termplotlib as tpl


def test_scatter():
    rng = np.random.default_rng(0)
    x = np.arange(0.0, 50.0, 2.0)
    y = x ** 1.3 + rng.random(x.shape) * 30.0

    fig = tpl.figure()
    fig.plot(x, y, plot_command="plot '-' w points", width=50, height=15)
    # fig.show()
    string = fig.get_string()

    ref = """\
  180 +---------------------------------------+
  160 |                                  A AA |
  140 |                                       |
      |                             A   A     |
  120 |                         AA A  A       |
  100 |                     A                 |
   80 |                  A    A               |
   60 |             A A    A                  |
      |       A AA A    A                     |
   40 |     A                                 |
   20 | A  A                                  |
    0 +---------------------------------------+
      0   5   10  15  20  25  30  35  40  45  50"""

    assert string == ref, string


if __name__ == "__main__":
    test_scatter()
