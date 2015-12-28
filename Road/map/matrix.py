# -*- coding: utf-8 -*-

__author__ = 'tobin'

import numpy as np
import cv2

def getTransformMatrix():
    # origin points
    rect = [(158, 334), (106, 350), (766, 377), (671, 361)]
    rect = np.array(rect, dtype = "float32")

    # destination points
    w, h = 800, 800
    dst = [(0, 0), (0, 50), (324, 60), (295, 31)]
    dst = np.array(dst, dtype = "float32")
    dst[:, 0] += 250
    dst[:, 1] += 360

    # return result & size
    M = cv2.getPerspectiveTransform(rect, dst)
    return M, (w, h)

def invertTransformMatrix():
    # origin points
    w, h = 800, 800
    dst = [(0, 0), (0, 50), (324, 60), (295, 31)]
    dst = np.array(dst, dtype = "float32")
    dst[:, 0] += 250
    dst[:, 1] += 360

    # destination points
    rect = [(158, 334), (106, 350), (766, 377), (671, 361)]
    rect = np.array(rect, dtype = "float32")

    # return result & size
    M = cv2.getPerspectiveTransform(dst, rect)
    return M, (w, h)