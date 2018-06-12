# asciiplotlib

[![CircleCI](https://img.shields.io/circleci/project/github/nschloe/asciiplotlib/master.svg)](https://circleci.com/gh/nschloe/asciiplotlib)
[![codecov](https://img.shields.io/codecov/c/github/nschloe/asciiplotlib.svg)](https://codecov.io/gh/nschloe/asciiplotlib)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)
[![PyPi Version](https://img.shields.io/pypi/v/asciiplotlib.svg)](https://pypi.org/project/asciiplotlib)
[![GitHub stars](https://img.shields.io/github/stars/nschloe/asciiplotlib.svg?logo=github&label=Stars)](https://github.com/nschloe/asciiplotlib)


no requirements!


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
