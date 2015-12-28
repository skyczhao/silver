# -*- coding: utf-8 -*-

__author__ = 'tobin'

from skimage import morphology
import numpy as np
import cv2

def get_skeleton(region):
    result = cv2.threshold(region, 0, 255, cv2.THRESH_OTSU)[1]
    result = morphology.skeletonize(result > 0)
    result = result.astype(np.uint8) * 255
    return result