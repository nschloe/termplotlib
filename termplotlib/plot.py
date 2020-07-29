import subprocess


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
    plot_command="plot '-' w lines",
    ticks_scale=0,
):
    p = subprocess.Popen(
        ["gnuplot"],
        stdout=subprocess.PIPE,
        stdin=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )

    gnuplot_input = []

    gnuplot_input.append(f"set term dumb mono {width},{height}")
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

    string = plot_command
    if label:
        string += f" title '{label}'"
    else:
        string += " notitle"

    gnuplot_input.append(string)

    for xx, yy in zip(x, y):
        gnuplot_input.append(f"{xx:e} {yy:e}")
    gnuplot_input.append("e")

    out = p.communicate(input="\n".join(gnuplot_input).encode())[0]

    return _remove_empty_lines(out.decode())


def _remove_empty_lines(string):
    return string.split("\n")[1:-2]
