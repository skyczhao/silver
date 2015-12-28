# -*- coding: utf-8 -*-
# $File: face.py
# $Date: Apr 1, 15:00, 2015.

__author__ = 'tobin'

import cv2
import numpy as np


def get_face_region(image, landmarks):
    """ get face region by landmarks

    :param image:
    :param landmarks:
    :return:
        faceRegion
    """

    # get image shape
    height, width = image.shape[:2]

    contour = landmarks['contour']
    # pick out the face contour in circular order
    contour_landmark = []
    # left part, in ascending order
    for i in range(1, 10):
        key = "contour_left" + str(i)
        contour_landmark.append([contour[key]["x"], contour[key]["y"]])
    # chin
    contour_landmark.append([contour["contour_chin"]["x"], contour["contour_chin"]["y"]])
    # right part, in descending order
    for i in range(9, 0, -1):
        key = "contour_right" + str(i)
        contour_landmark.append([contour[key]["x"], contour[key]["y"]])
    # transform the rate to real position
    contour = np.array(contour_landmark)
    contour[:, 0] = contour[:, 0] * width / 100
    contour[:, 1] = contour[:, 1] * height / 100

    # draw lines on new canvas
    faceRegion = np.zeros(image.shape[:2], np.uint8)
    length = len(contour)
    for current in range(length):
        next = (current + 1) % length
        start_point = (int(contour[current][0]), int(contour[current][1]))
        end_point = (int(contour[next][0]), int(contour[next][1]))
        cv2.line(faceRegion, start_point, end_point, 255, 1)
    # flood fill the contour
    seed = (300, 450)  # TODO: better choice?
    mask = np.zeros((height + 2, width + 2), np.uint8)
    cv2.floodFill(faceRegion, mask, seed, 255)

    return faceRegion
