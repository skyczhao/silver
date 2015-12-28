# -*- coding: utf-8 -*-
# $File: eye.py
# $Date: Mar 31, 20:30, 2015.

__author__ = 'tobin'

import cv2
import numpy as np


def get_eye_region(image, landmarks):
    """ get eye region

    :param image:
    :param landmarks:
    :return:
        eyeRegion:
    """

    # image shape
    height, width = image.shape[:2]

    # pick out eye region
    region = np.zeros(image.shape[:2], np.uint8)
    # pick out left eye
    left_eye_marks = landmarks["left_eye"]
    for (key, value) in left_eye_marks.items():
        value["x"] = value["x"] * width / 100
        value["y"] = value["y"] * height / 100
        cv2.circle(region, (int(value["x"]), int(value["y"])), 15, 255, -1)
    # pick out right eye
    right_eye_marks = landmarks["right_eye"]
    for (key, value) in right_eye_marks.items():
        value["x"] = value["x"] * width / 100
        value["y"] = value["y"] * height / 100
        cv2.circle(region, (int(value["x"]), int(value["y"])), 15, 255, -1)

    # return eye region
    return region