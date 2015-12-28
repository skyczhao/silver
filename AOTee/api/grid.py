# -*- coding: utf-8 -*-
# $File: grid.py
# $Date: Apr 3, 16:30, 2015.

__author__ = 'tobin'

import numpy as np


def get_grid_feature(mask, splitSize):
    """ split the mask and calculate the pixel rate of each sub-part

    :param mask:
    :param splitSize:
    :return:
    """

    # the result
    feature = []
    # split the mask into multiple sub-rows
    rows = np.vsplit(mask, splitSize)
    for row in rows:
        feature_row = []
        # split the sub-row into multiple sub-cols
        cols = np.hsplit(row, splitSize)
        for col in cols:
            h, w = col.shape
            nums = (col > 0).sum()
            # calculate the pixel rate
            rate = nums / float(h * w)

            # append the col rate into row feature
            feature_row.append(rate)
        # append the row feature into the whole feature
        feature.append(feature_row)

    # return result
    return np.array(feature)