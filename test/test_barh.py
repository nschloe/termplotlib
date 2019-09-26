import sys

import pytest

import termplotlib as tpl


@pytest.mark.skipif(
    sys.stdout.encoding not in ["UTF-8", "UTF8"],
    reason="Need UTF-8 terminal (not {})".format(sys.stdout.encoding),
)
def test_barh():
    fig = tpl.figure()
    fig.barh([3, 10, 5, 2], ["Cats", "Dogs", "Cows", "Geese"])
    # fig.show()
    string = fig.get_string()

    assert (
        string
        == """\
Cats   [ 3]  ████████████
Dogs   [10]  ████████████████████████████████████████
Cows   [ 5]  ████████████████████
Geese  [ 2]  ████████\
"""
    )
    return


def test_barh_ascii():
    fig = tpl.figure()
    fig.barh([3, 10, 5, 2], ["Cats", "Dogs", "Cows", "Geese"], force_ascii=True)
    # fig.show()
    string = fig.get_string()

    assert (
        string
        == """\
Cats   [ 3]  ************
Dogs   [10]  ****************************************
Cows   [ 5]  ********************
Geese  [ 2]  ********\
"""
    )
    return


@pytest.mark.skipif(
    sys.stdout.encoding not in ["UTF-8", "UTF8"],
    reason="Need UTF-8 terminal (not {})".format(sys.stdout.encoding),
)
def test_barh_floats():
    fig = tpl.figure()
    fig.barh([0.3, 0.4, 0.6, 0.2], ["Cats", "Dogs", "Cows", "Geese"])
    # fig.show()
    string = fig.get_string()

    assert (
        string
        == """\
Cats   [0.3]  ████████████████████
Dogs   [0.4]  ██████████████████████████▋
Cows   [0.6]  ████████████████████████████████████████
Geese  [0.2]  █████████████▍\
"""
    )
    return


if __name__ == "__main__":
    # test_horizontal_ascii()
    # test_barh()
    test_barh_floats()
