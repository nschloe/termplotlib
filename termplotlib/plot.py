import subprocess
import numpy as np
import ipdb as pdb

def is_array(v):
    return (type(v) is list or type(v) is np.ndarray or type(v) is tuple)

def plot(
    x,
    y,
    width=80,
    height=25,
    label=None,
    xlim=None,
    ylim=None,
    xlabel=None,
    title=None,
    extra_gnuplot_arguments=None,
    gnuplot_term_arguments='',
    plot_command="plot $data w lines",
    ticks_scale=0,
):
    p = subprocess.Popen(
        ["gnuplot"],
        stdout=subprocess.PIPE,
        stdin=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    plot_multi_count = None

    gnuplot_input = []

    ###########################################################################
    # Prepare heredoc in gnuplot
    # If multiple plots in y as a list of lists or a multi-dim numpy array
    # We will send out the plots separated by blank lines for gnuplot
    gnuplot_input.append("$data <<EOD")
    if (is_array(y) and is_array(y[0])):
        plot_multi_count = len(y)
        for plot_i in range(len(y)):
            for xx, yy in zip(x, y[plot_i]):
                gnuplot_input.append(f"{xx:e} {yy:e}")
            gnuplot_input.append("")
    else: # Single plot provided by caller
        for xx, yy in zip(x, y):
            gnuplot_input.append(f"{xx:e} {yy:e}")
    gnuplot_input.append("EOD")

    ###########################################################################
    gnuplot_input.append("set colorsequence classic")
    gnuplot_input.append(f"set term dumb {width},{height} {gnuplot_term_arguments}")
    # gnuplot_input.append("set tics nomirror")
    gnuplot_input.append(f"set tics scale {ticks_scale}")

    if xlim:
        gnuplot_input.append("set xrange [{}:{}]".format(xlim[0], xlim[1]))

    if ylim:
        gnuplot_input.append("set yrange [{}:{}]".format(ylim[0], ylim[1]))

    if xlabel:
        gnuplot_input.append(f'set xlabel "{xlabel}"')

    if title:
        gnuplot_input.append(f'set title "{title}"')

    if extra_gnuplot_arguments:
        gnuplot_input += extra_gnuplot_arguments

    if plot_multi_count is None:
        string = plot_command
        if label:
            string += f" title '{label}'"
        else:
            string += " notitle"
    else:
        string = "plot"
        string += ", ".join(
            [f"$data every:::{i}::{i} w lines title '{i}'" for i in range(plot_multi_count)])

    gnuplot_input.append(string)

    out = p.communicate(input="\n".join(gnuplot_input).encode())[0]

    return _remove_empty_lines(out.decode())


def _remove_empty_lines(string):
    return string.split("\n")[1:-2]
