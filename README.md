# termplotlib

[![CircleCI](https://img.shields.io/circleci/project/github/nschloe/termplotlib/master.svg)](https://circleci.com/gh/nschloe/termplotlib)
[![codecov](https://img.shields.io/codecov/c/github/nschloe/termplotlib.svg)](https://codecov.io/gh/nschloe/termplotlib)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![PyPi Version](https://img.shields.io/pypi/v/termplotlib.svg)](https://pypi.org/project/termplotlib)
[![GitHub stars](https://img.shields.io/github/stars/nschloe/termplotlib.svg?logo=github&label=Stars&logoColor=white)](https://github.com/nschloe/termplotlib)
[![PyPi downloads](https://img.shields.io/pypi/dm/termplotlib.svg)](https://pypistats.org/packages/termplotlib)

termplotlib is a Python library for all your terminal plotting needs. It aims to work
like [matplotlib](https://matplotlib.org/).


### Line plots

For line plots, termplotlib relies on [gnuplot](http://www.gnuplot.info/). With that installed, the code
```python
import termplotlib as tpl
import numpy

x = numpy.linspace(0, 2 * numpy.pi, 10)
y = numpy.sin(x)

fig = tpl.figure()
fig.plot(x, y, label="data", width=50, height=15)
fig.show()
```
produces
```
    1 +---------------------------------------+
  0.8 |    **     **                          |
  0.6 |   *         **           data ******* |
  0.4 | **                                    |
  0.2 |*              **                      |
    0 |                 **                    |
      |                                   *   |
 -0.2 |                   **            **    |
 -0.4 |                     **         *      |
 -0.6 |                              **       |
 -0.8 |                       **** **         |
   -1 +---------------------------------------+
      0     1    2     3     4     5    6     7
```

### Horizontal histograms

```python
import termplotlib as tpl
import numpy

numpy.random.seed(123)
sample = numpy.random.normal(size=1000)
counts, bin_edges = numpy.histogram(sample)

fig = tpl.figure()
fig.hist(counts, bin_edges, orientation="horizontal", force_ascii=False)
fig.show()
```
produces

![hist1](https://nschloe.github.io/termplotlib/hist1.png)

Horizontal bar charts are covered as well. This
```python
fig = tpl.figure()
fig.barh(
    [3, 10, 5, 2],
    ['Cats', 'Dogs', 'Cows', 'Geese'],
    force_ascii=True
)
fig.show()
```
produces
```
Cats   [ 3]  ************
Dogs   [10]  ****************************************
Cows   [ 5]  ********************
Geese  [ 2]  ********
```

### Vertical histograms

```python
import termplotlib as tpl
import numpy

numpy.random.seed(123)
sample = numpy.random.normal(size=1000)
counts, bin_edges = numpy.histogram(sample, bins=40)
fig = tpl.figure()
fig.hist(counts, bin_edges, grid=[15, 25], force_ascii=False)
fig.show()
```
produces

![hist2](https://nschloe.github.io/termplotlib/hist2.png)


### Tables

Support for tables has moved over to
[termtables](https://github.com/nschloe/termtables).


### Installation

termplotlib is [available from the Python Package
Index](https://pypi.org/project/termplotlib/), so simply do
```
pip3 install -U termplotlib
```
to install or upgrade. Use `sudo -H` to install as root or the `--user` option
of `pip3` to install in `$HOME`.


### Testing

To run the termplotlib unit tests, check out this repository and type
```
pytest
```

### License

termplotlib is published under the [MIT license](https://en.wikipedia.org/wiki/MIT_License).
