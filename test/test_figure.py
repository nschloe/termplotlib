# -*- coding: utf-8 -*-
#
import termiplot as tp


def test_simple():
    fig = tp.figure()
    fig.aprint("abc")
    string = fig.get_string()
    assert string == """abc"""
    return


def test_padding_1():
    fig = tp.figure(padding=1)
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
    fig = tp.figure(padding=(1,))
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
    fig = tp.figure(padding=(1, 2))
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
    fig = tp.figure(padding=(1, 2, 3))
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
    fig = tp.figure(padding=(1, 2, 3, 4))
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
