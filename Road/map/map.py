# -*- coding: utf-8 -*-

__author__ = 'tobin'

import numpy as np
import cv2

import matrix

def get_perspective(image):
    M, size = matrix.getTransformMatrix()
    warped = cv2.warpPerspective(image, M, size)

    return warped

def invert_perspective(image):
    M, size = matrix.invertTransformMatrix()
    origin = cv2.warpPerspective(image, M, size)

    return origin