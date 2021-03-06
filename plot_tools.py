# -*- coding: utf-8 -*-
r"""
Created on Mon Aug 20 13:36:57 2018

@author: F. Obersteiner, florian\obersteiner\\kit\edu
"""

import numpy as np

###############################################################################


def get_plot_range(v, add_percent=5, v_min_lim=False, v_max_lim=False,
                   xrange=False, x=False):
    """
    Adjust y-axis range of matplotlib pyplot for a given vector v.

    Parameters
    ----------
    v : list or numpy 1d array
        dependent variable.
    add_percent : numeric type scalar value, optional
        percent of the range of v that should be added to result. The default is 5.
    v_min_lim : numeric type scalar value, optional
        minimum value for lower yrange limit. The default is False.
    v_max_lim : numeric type scalar value, optional
        maximum value for upper yrange limit. The default is False.
    xrange : list, optional
        [lower_limit, upper_limit] of independent variable. The default is False.
    x : list or numpy 1d array, optional
        independent variable. The default is False.

    Returns
    -------
    result : list
        lower and upper limit.

    """

    if x and xrange:
        x = np.array(sorted(x)) # monotonically increasing x-vector (e.g. time)
        if len(x) == len(v):
            w_xvd = np.where((x >= xrange[0]) & (x <= xrange[1]))
            v = v[w_xvd]

    v = list(filter(lambda x: x is not None, v))
    v = np.array(v)[np.isfinite(np.array(v))]

    if len(v) < 2:
        result = None
    else:
        result = [1, 1]
        v_min = min(v)
        v_max = max(v)
        offset = (abs(v_min)+abs(v_max))/2 * add_percent/100
        result[0] = v_min - offset
        result[1] = v_max + offset

        if v_min_lim is not False:
            if result[0] < v_min_lim:
                result[0] = v_min_lim

        if v_max_lim is not False:
            if result[1] > v_max_lim:
                result[1] = v_max_lim

    return result


###############################################################################
