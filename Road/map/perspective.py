# -*- coding: utf-8 -*-

__author__ = 'tobin'

import cv2
import math
import numpy as np

import tdrotate

def rotate(radian, center, image):
    alpha, beta, _ = radian
    x, y = center
    x = int(x)
    y = int(y)
    height, width = image.shape[:2]

    # split the image
    u_l = image[:y, :x, :]
    u_r = image[:y, x:width, :]
    d_l = image[y:height, :x, :]
    d_r = image[y:height, x:width, :]

    # perspective mapping
    u_l = subrotate(u_l, (-alpha, -beta, 0), 2)
    u_r = subrotate(u_r, (-beta, alpha, 0), 3)
    d_l = subrotate(d_l, (beta, -alpha, 0), 1)
    d_r = subrotate(d_r, (alpha, beta, 0), 0)

    # merge
    result = np.zeros((height * 2, width * 2, 3), np.uint8)
    x *= 2
    y *= 2
    height, width = result.shape[:2]
    result[:y, :x, :] = u_l
    result[:y, x:width, :] = u_r
    result[y:height, :x, :] = d_l
    result[y:height, x:width, :] = d_r

    # calculate padding
    p_l = 0
    for i in range(width):
        if np.amax(result[:, i, :]) != 0:
            p_l = i
            break
    p_t = 0
    for i in range(height):
        if np.amax(result[i, :, :]) != 0:
            p_t = i
            break
    p_r = 0
    for i in range(width, 0, -1):
        if np.amax(result[:, i - 1, :]) != 0:
            p_r = i - 1
            break
    p_d = 0
    for i in range(height, 0, -1):
        if np.amax(result[i - 1, :, :]) != 0:
            p_d = i - 1
            break

    return result[p_t:p_d, p_l:p_r, :], (x - p_l, y - p_t)

def subrotate(image, radian, times):
    R, _ = tdrotate.matrix(radian, (0, 0))

    tmp = tdrotate.rotate90(image, times)
    height, width = tmp.shape[:2]
    tmp = cv2.warpPerspective(tmp, R, (width * 2, height * 2))
    result = tdrotate.rotate90(tmp, 4 - times)

    return result
