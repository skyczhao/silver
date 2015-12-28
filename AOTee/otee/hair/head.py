# -*- coding: utf-8 -*-
# $File: head.py
# $Date: Mar 26, 16:30, 2015.

__author__ = 'tobin'

import numpy as np

import cv2


def get_head_region(image, faceRegion):
    """ detect head region by face region

    :param image:
    :param faceRegion:
    :return:
        headRegion: head region
    """

    # copy image, do not change the origin images
    face = image.copy()

    # TODO: using the landmarks to expand the head region

    # useful parameters
    height, width = face.shape[:2]
    size = 40                                 # the expanded kernel size
    kernel = np.ones((size, size), np.uint8)  # the expanded kernel
    pad = 5                                   # the impossible head area padding size

    # remove the background
    # TODO: alpha matting?
    # 1: expand the possible head region
    # expand the face region to cover the head
    biger = cv2.dilate(faceRegion, kernel)
    biger = cv2.dilate(biger, kernel)
    # 2: using grabcut to remove the impossible head region
    # the expanded region maybe the head region
    mask = np.where(biger > 0, cv2.GC_PR_FGD, cv2.GC_PR_BGD).astype('uint8')
    # the padding area must be the background
    mask[:, 0:pad] = cv2.GC_BGD
    mask[0:pad, :] = cv2.GC_BGD
    mask[:, width-pad:width] = cv2.GC_BGD
    mask[height-pad:height, :] = cv2.GC_BGD
    # other useless grabcut parameter
    back = np.zeros((1, 65), np.float64)
    fore = np.zeros((1, 65), np.float64)
    rect = (0, 0, 0, 0)
    # grabcut to detect the background
    cv2.grabCut(face, mask, rect, back, fore, 1, cv2.GC_INIT_WITH_MASK)
    # select the foreground only
    foreground = np.where((mask == cv2.GC_FGD) + (mask == cv2.GC_PR_FGD), 255, 0).astype('uint8')

    # pick the head from foreground
    # separate the connected area
    narrow = cv2.erode(foreground, kernel)
    contours, hierarchy = cv2.findContours(narrow.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # find the max area region
    max = 0
    max_index = 0
    for i, c in enumerate(contours):
        area = cv2.contourArea(c)
        if area > max:
            max = area
            max_index = i
    headRegion = np.zeros(image.shape[:2], np.uint8)
    cv2.drawContours(headRegion, contours, max_index, 255, -1)
    # restore the erode image
    headRegion = cv2.dilate(headRegion, kernel)

    return headRegion