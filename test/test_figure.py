# -*- coding: utf-8 -*-
#
import asciiplotlib as apl


def test_simple():
    fig = apl.figure()
    fig.aprint("abc")
    string = fig.get_string()
    assert string == """abc"""
    return


def test_padding_1():
    fig = apl.figure(padding=1)
    fig.aprint("abc")
    string = fig.get_string()
    assert (
        string
        == """
 abc
"""
    )
    return


def test_padding_1b():
    fig = apl.figure(padding=(1,))
    fig.aprint("abc")
    string = fig.get_string()
    assert (
        string
        == """
 abc
"""
    )
    return


def test_padding_2():
    fig = apl.figure(padding=(1, 2))
    fig.aprint("abc")
    string = fig.get_string()
    assert (
        string
        == """
  abc
"""
    )
    return


def test_padding_3():
    fig = apl.figure(padding=(1, 2, 3))
    fig.aprint("abc")
    string = fig.get_string()
    assert (
        string
        == """
  abc


"""
    )
    return


def test_padding_4():
    fig = apl.figure(padding=(1, 2, 3, 4))
    fig.aprint("abc")
    string = fig.get_string()
    assert (
        string
        == """
    abc


"""
    )
    fig.show()
    return
