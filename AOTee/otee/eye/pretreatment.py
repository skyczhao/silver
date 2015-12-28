# -*- coding: utf-8 -*-
# $File: pretreatment.py
# $Date: May, 7th. 11:50, 2015.

__author__ = 'tobin'

import cv2
import numpy as np


def myotee_process(eye):
    """ myotee eye pretreatment

    :param eye:
    :return:
        result
    """

    # expand by copy
    result = cv2.copyMakeBorder(eye, 60, 60, 60, 60, cv2.BORDER_REPLICATE)
    # resize to fixed size
    result = cv2.resize(result, (600, 600))
    # handle single panel image
    if len(result.shape) < 3:
        alpha = np.where(result == 255, 0, 255).astype("uint8")
        x, y = np.where(alpha != 0)
        for i, j in zip(x, y):
            alpha[i, j] = 255 - result[i, j]
        result = np.dstack([result, result, result, alpha])

    return result