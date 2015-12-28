# -*- coding: utf-8 -*-
# $File: skin.py
# $Date: Mar 29, 10:50, 2015.

__author__ = 'tobin'

import cv2
import numpy as np


def get_skin_region(image):
    """ detect the skin color region from image

    :param image:
    :return:
        skinRegion: the skin similar color region
    """

    # copy image to process
    # do not change the origin images
    face = image.copy()

    # skin color range
    min_YCrCb = np.array([0, 133, 77], np.uint8)
    max_YCrCb = np.array([255, 173, 127], np.uint8)

    # color balance for better detection
    meanRGB = cv2.mean(face)[:3]
    minAVG = np.amin(meanRGB)
    for i in range(0, 3):
        face[:, :, i] = face[:, :, i] * minAVG / meanRGB[i]

    # cover RGB to YCrCb
    imageYCrCb = cv2.cvtColor(face, cv2.COLOR_BGR2YCR_CB)
    # using color segmentation to detect skin similar region
    skinRegion = cv2.inRange(imageYCrCb, min_YCrCb, max_YCrCb)

    return skinRegion