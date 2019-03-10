# termiplot

[![CircleCI](https://img.shields.io/circleci/project/github/nschloe/termiplot/master.svg)](https://circleci.com/gh/nschloe/termiplot)
[![codecov](https://img.shields.io/codecov/c/github/nschloe/termiplot.svg)](https://codecov.io/gh/nschloe/termiplot)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)
[![PyPi Version](https://img.shields.io/pypi/v/termiplot.svg)](https://pypi.org/project/termiplot)
[![GitHub stars](https://img.shields.io/github/stars/nschloe/termiplot.svg?logo=github&label=Stars&logoColor=white)](https://github.com/nschloe/termiplot)

termiplot is a Python 3 library for all your terminal plotting needs. It aims to work
like [matplotlib](https://matplotlib.org/).


### Line plots

For line plots, termiplot relies on [gnuplot](http://www.gnuplot.info/). With that installed, the code
```python
import termiplot as tp
import numpy

x = numpy.linspace(0, 2 * numpy.pi, 10)
y = numpy.sin(x)

fig = tp.figure()
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


### Tables

termiplot provides many options for table plotting. For the most basic example, the
code
```python
import termiplot as tp
import numpy

numpy.random.seed(0)
data = numpy.random.rand(5, 2)

fig = tp.figure()
fig.table(data)
fig.show()
```
produces

![table1](https://nschloe.github.io/termiplot/table1.png)

You can control border style, padding, alignment, and various other attributes. For
example,
```python
import termiplot as tp

data = [
    [["a", "bb", "ccc"]],
    [[1, 2, 3], [613.23236243236, 613.23236243236, 613.23236243236]],
]

fig = tp.figure()
fig.table(data, border_style="thin", force_ascii=True, padding=(0, 1), alignment="lcr")
fig.show()
```
produces
```
+-----------------+-----------------+-----------------+
| a               |       bb        |             ccc |
+=================+=================+=================+
| 1               |        2        |               3 |
+-----------------+-----------------+-----------------+
| 613.23236243236 | 613.23236243236 | 613.23236243236 |
+-----------------+-----------------+-----------------+
```
See
[`test/test_table.py`](https://github.com/nschloe/termiplot/blob/master/test/test_table.py)
for more examples.


### Horizontal histograms

```python
import termiplot as tp
import numpy

numpy.random.seed(123)
sample = numpy.random.normal(size=1000)
counts, bin_edges = numpy.histogram(sample)

fig = tp.figure()
fig.hist(counts, bin_edges, orientation="horizontal", force_ascii=False)
fig.show()
```
produces

![hist1](https://nschloe.github.io/termiplot/hist1.png)

### Vertical histograms

```python
import termiplot as tp
import numpy

numpy.random.seed(123)
sample = numpy.random.normal(size=1000)
counts, bin_edges = numpy.histogram(sample, bins=40)
fig = tp.figure()
fig.hist(counts, bin_edges, grid=[15, 25], force_ascii=False)
fig.show()
```
produces

![hist2](https://nschloe.github.io/termiplot/hist2.png)

### Installation

termiplot is [available from the Python Package
Index](https://pypi.org/project/termiplot/), so simply do
```
pip3 install -U termiplot
```
to install or upgrade. Use `sudo -H` to install as root or the `--user` option
of `pip3` to install in `$HOME`.


### Testing

To run the termiplot unit tests, check out this repository and type
```
pytest
```

### Distribution
To create a new release

1. bump the `__version__` number,

2. publish to PyPi and tag on GitHub:
    ```
    $ make publish
    ```

### License

termiplot is published under the [MIT license](https://en.wikipedia.org/wiki/MIT_License).
