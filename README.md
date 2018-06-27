# asciiplotlib

[![CircleCI](https://img.shields.io/circleci/project/github/nschloe/asciiplotlib/master.svg)](https://circleci.com/gh/nschloe/asciiplotlib)
[![codecov](https://img.shields.io/codecov/c/github/nschloe/asciiplotlib.svg)](https://codecov.io/gh/nschloe/asciiplotlib)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)
[![PyPi Version](https://img.shields.io/pypi/v/asciiplotlib.svg)](https://pypi.org/project/asciiplotlib)
[![GitHub stars](https://img.shields.io/github/stars/nschloe/asciiplotlib.svg?logo=github&label=Stars)](https://github.com/nschloe/asciiplotlib)

asciiplotlib is a Python library for all your terminal plotting needs.


### Line plots
```
import asciiplotlib as apl

x = numpy.linspace(0, 2 * numpy.pi, 10)
y = numpy.sin(x)

fig = apl.figure()
fig.plot(x, y, label="data", width=50, height=15)
fig.show()
```
produces
```

    1 +---------------------------------------+
  0.8 |-+  **    +A*   +     +     +    +   +-|
  0.6 |-+ A         **           data ***A***-|
  0.4 |-**                                  +-|
  0.2 |*+             A*                    +-|
    0 |-+               **                  +-|
      |                                   A   |
 -0.2 |-+                 A*            **  +-|
 -0.4 |-+                   **         *    +-|
 -0.6 |-+                            *A     +-|
 -0.8 |-+   +    +     +     +A*** **   +   +-|
   -1 +---------------------------------------+
      0     1    2     3     4     5    6     7

```
Here, asciiplotlib relies on [gnuplot](http://www.gnuplot.info/).


### Tables

asciiplotlib
```python
import asciiplotlib as apl

numpy.random.seed(0)
data = numpy.random.rand(5, 2)

fig = apl.figure()
fig.table(data)
fig.show()
```
produces
```
┌────────────────────┬────────────────────┐
│ 0.5488135039273248 │ 0.7151893663724195 │
├────────────────────┼────────────────────┤
│ 0.6027633760716439 │ 0.5448831829968969 │
├────────────────────┼────────────────────┤
│ 0.4236547993389047 │ 0.6458941130666561 │
├────────────────────┼────────────────────┤
│ 0.4375872112626925 │ 0.8917730007820798 │
├────────────────────┼────────────────────┤
│ 0.9636627605010293 │ 0.3834415188257777 │
└────────────────────┴────────────────────┘
```
There are many options for the table plotter, e.g.,
```python
import asciiplotlib as apl

data = [
    [["a", "bb", "ccc"]],
    [[1, 2, 3], [613.23236243236, 613.23236243236, 613.23236243236]],
]

fig = apl.figure()
fig.table(data, border_style="thin", ascii_mode=True, padding=(0, 1), alignment="lcr")
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
[`test/test_table.py`](https://github.com/nschloe/asciiplotlib/blob/master/test/test_table.py)
for more examples.


### Horizontal histograms

```python
import asciiplotlib as apl

numpy.random.seed(123)
sample = numpy.random.normal(size=1000)
counts, bin_edges = numpy.histogram(sample)

fig = apl.figure()
fig.hist(counts, bin_edges, orientation="horizontal")
fig.show()
```
produces
```
-3.23e+00 - -2.55e+00  [  7]  █
-2.55e+00 - -1.87e+00  [ 27]  ███▊
-1.87e+00 - -1.19e+00  [ 95]  █████████████▎
-1.19e+00 - -5.10e-01  [183]  █████████████████████████▋
-5.10e-01 - +1.70e-01  [286]  ████████████████████████████████████████
+1.70e-01 - +8.51e-01  [202]  ████████████████████████████▎
+8.51e-01 - +1.53e+00  [142]  ███████████████████▉
+1.53e+00 - +2.21e+00  [ 49]  ██████▉
+2.21e+00 - +2.89e+00  [  7]  █
+2.89e+00 - +3.57e+00  [  2]  ▎
```

#### Vertical histograms

```python
import asciiplotlib as apl

numpy.random.seed(123)
sample = numpy.random.normal(size=1000)
counts, bin_edges = numpy.histogram(sample)

fig = apl.figure()
fig.hist(counts, bin_edges, grid=[5, 8])
fig.show()
```
produces
```
    █
    █
    ▉▁
   ▃▉█
   █▉█
   █▉██
  ▃█▉██
  ██▉██
  ██▉██▆
▂███▉██▉▂▁
```

### Installation

asciiplotlib is [available from the Python Package
Index](https://pypi.org/project/asciiplotlib/), so simply do
```
pip install -U asciiplotlib
```
to install or upgrade. Use `sudo -H` to install as root or the `--user` option
of `pip` to install in `$HOME`.


### Testing

To run the asciiplotlib unit tests, check out this repository and type
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

asciiplotlib is published under the [MIT license](https://en.wikipedia.org/wiki/MIT_License).
