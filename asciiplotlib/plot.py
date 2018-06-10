# -*- coding: utf-8 -*-
#
import subprocess


def plot(x, y, width=80, height=25, title=None, xlim=None, ylim=None):
    p = subprocess.Popen(
        ["gnuplot"],
        stdout=subprocess.PIPE,
        stdin=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )

    gnuplot_input = ["set term dumb {} {}".format(width, height)]

    if xlim:
        gnuplot_input.append("set xrange [{}:{}]".format(xlim[0], xlim[1]))

    if ylim:
        gnuplot_input.append("set yrange [{}:{}]".format(ylim[0], ylim[1]))

    string = "plot '-' using 1:2 with linespoints"
    if title:
        string += " title '{}'".format(title)

    gnuplot_input.append(string)

    for xx, yy in zip(x, y):
        gnuplot_input.append("{:e} {:e}".format(xx, yy))
    gnuplot_input.append("e")

    out = p.communicate(input="\n".join(gnuplot_input).encode())[0]

    return out.decode().split("\n")
