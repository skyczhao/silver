# -*- coding: utf-8 -*-
# $File: detect.py
# $Date: Mar 29, 10:50, 2015.

__author__ = 'tobin'

import numpy as np

import cv2

from api.skin import get_skin_region


def get_face_region(image):
    """ detect face from human image

    :param image:
    :return:
        faceRegion: face region
    """

    # First: find the skin color region
    skinRegion = get_skin_region(image)

    # Second: find the face from skin color region
    # search contours from skin color region
    faceRegions = np.zeros(skinRegion.shape[:2], np.uint8)
    contours, hierarchy = cv2.findContours(skinRegion, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # the face region area must be larger than 1000
    for i, c in enumerate(contours):
        area = cv2.contourArea(c)
        if area > 1000:  # TODO: Better choice?
            cv2.drawContours(faceRegions, contours, i, 255, -1)
    # flood fill algorithm to select the main face in the image center
    height, width = faceRegions.shape[:2]
    seed = (width / 2, height / 2)  # TODO: select better seed
    mask = np.zeros((height + 2, width + 2), np.uint8)
    # set a special color
    cv2.floodFill(faceRegions, mask, seed, 127)

    # Final: redraw the main face from special color
    faceRegion = np.where(faceRegions == 127, 255, 0).astype('uint8')

    return faceRegion