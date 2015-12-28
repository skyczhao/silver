# -*- coding: utf-8 -*-

__author__ = 'tobin'

import math
import numpy as np
import cv2

def matrix(radian, position):
    alpha, beta, gama = radian
    x, y = position

    # =====      Begin      =====
    # ===== Not Change Them =====
    sin_alpha = math.sin(alpha)
    cos_alpha = math.cos(alpha)

    sin_beta = math.sin(beta)
    cos_beta = math.cos(beta)

    sin_gama = math.sin(gama)
    cos_gama = math.cos(gama)

    R = np.array([[cos_beta * cos_gama,
                   cos_beta * sin_gama,
                   -sin_beta],
                  [sin_alpha * sin_beta * cos_gama - cos_alpha * sin_gama,
                   sin_alpha * sin_beta * sin_gama + cos_alpha * cos_gama,
                   sin_alpha * cos_beta],
                  [cos_alpha * sin_beta * cos_gama + sin_alpha * sin_gama,
                   cos_alpha * sin_beta * sin_gama - sin_alpha * cos_gama,
                   cos_alpha * cos_beta]])

    T = np.array([[1.0, 0.0, -x],
                  [0.0, 1.0, -y]])
    # ===== Not Change Them =====
    # =====       End       =====

    return R, T


def rotate90(image, times = 1):
    # get rotate 90 degree times
    times = int(times) % 4

    # cases
    if times == 0:
        # not change
        result = image.copy()
    elif times == 1:
        # 90 degree
        trans = cv2.transpose(image)
        result = cv2.flip(trans, 0)
    elif times == 2:
        # 180 degree
        result = cv2.flip(image, -1)
    else:
        # 270 or -90 degree
        trans = cv2.transpose(image)
        result = cv2.flip(trans, 1)

    return result