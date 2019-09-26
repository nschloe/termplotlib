import termplotlib as tpl


def test_simple():
    fig = tpl.figure()
    fig.aprint("abc")
    string = fig.get_string()
    assert string == """abc"""
    return


def test_padding_1():
    fig = tpl.figure(padding=1)
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
    fig = tpl.figure(padding=(1,))
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
    fig = tpl.figure(padding=(1, 2))
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
    fig = tpl.figure(padding=(1, 2, 3))
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
    fig = tpl.figure(padding=(1, 2, 3, 4))
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
