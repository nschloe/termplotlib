import numpy

import termplotlib as tpl


def test_scatter():
    numpy.random.seed(0)
    x = numpy.arange(0.0, 50.0, 2.0)
    y = x ** 1.3 + numpy.random.rand(*x.shape) * 30.0

    fig = tpl.figure()
    fig.plot(x, y, plot_command="plot '-' w points", width=50, height=15)
    # fig.show()
    string = fig.get_string()

    ref = """  180 +---------------------------------------+
  160 |                                    AA |
  140 |                             A A AA    |
      |                          A A          |
  120 |                                       |
  100 |                    A    A             |
   80 |                  A  A A               |
   60 |          A A  A A                     |
      |             A                         |
   40 |    AA A A                             |
   20 | AA                                    |
    0 +---------------------------------------+
      0   5   10  15  20  25  30  35  40  45  50"""

    assert string == ref


if __name__ == "__main__":
    test_scatter()
