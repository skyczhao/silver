# -*- coding: utf-8 -*-
# $File: maskadd.py
# $Date: Apr 2, 16:30, 2015.

__author__ = 'tobin'

import numpy as np


def maskadd(dst, src, mask):
    """ add two image with mask

    :param dst:
    :param src:
    :param mask:
    :return:
        result:
    """

    # get needed pixel
    x, y = np.where(mask != 0)

    # ready the final result container
    result = dst.copy()
    # loop to add each needed pixel
    for i, j in zip(x, y):
        # using float to ensure the float result
        rate = mask[i, j] / 255.0
        tmp = src[i, j] * rate + result[i, j] * (1 - rate)
        # integer assignment
        result[i, j] = tmp.astype('uint8')

    # return
    return result