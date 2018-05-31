# -*- coding: utf-8 -*-
#
from __future__ import division, print_function

import numpy


def hist(a, orientation='horizontal', max_width=40, bins=20,
         show_counts=True, show_xticks=True):
    # ax2.hist(a, bins=30, orientation="horizontal")
    counts, bin_edges = numpy.histogram(a, bins=bins)
    averages = (bin_edges[:-1] + bin_edges[1:]) / 2

    max_count = numpy.max(counts)

    full = '\u2588'
    eighths = [
        '',
        '\u258f', '\u258e', '\u258d', '\u258c', '\u258b', '\u258a', '\u2589'
        ]

    for count, average in zip(counts, averages):
        width = count / max_count * max_width
        # Round to 0.125
        rwidth = int(round(width * 8))
        num_full_blocks = rwidth // 8
        remainder = rwidth % 8
        if show_xticks:
            print('{:+e}  '.format(average), end='')

        print(num_full_blocks * full + eighths[remainder], end='')
        if show_counts:
            fill_width = (
                max_width - (num_full_blocks + (1 if remainder > 0 else 0))
                )
            print(fill_width*' ' + '  {}'.format(count), end='')
        print()

    return
