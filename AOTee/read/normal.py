# -*- coding: utf-8 -*-
# $File: normal.py
# $Date: Mar 29, 20:00, 2015.

__author__ = 'tobin'

import cv2
import numpy as np
import copy


def normalize(image, landmarks):
    """ normalize the relative variables

    :param image:
    :param landmarks:
    :return:
        face: face image
        marks: landmarks
    """

    # copy image to avoid modification
    face = image.copy()
    marks = copy.deepcopy(landmarks)
    height, width = face.shape[:2]

    # perspective mapping reference points
    # right eye center
    right_eye_center = marks["right_eye"]["right_eye_center"]
    right_eye_center = (right_eye_center["x"] * width / 100, right_eye_center["y"] * height / 100)
    # left eye center
    left_eye_center = marks["left_eye"]["left_eye_center"]
    left_eye_center = (left_eye_center["x"] * width / 100, left_eye_center["y"] * height / 100)
    # mouth left corner
    mouth_left_corner = marks["mouth"]["mouth_left_corner"]
    mouth_left_corner = (mouth_left_corner["x"] * width / 100, mouth_left_corner["y"] * height / 100)
    # mouth right corner
    mouth_right_corner = marks["mouth"]["mouth_right_corner"]
    mouth_right_corner = (mouth_right_corner["x"] * width / 100, mouth_right_corner["y"] * height / 100)

    # origin reference points
    rect = [right_eye_center, left_eye_center, mouth_left_corner, mouth_right_corner]
    rect = np.array(rect, dtype = "float32")

    # destination reference points
    size = (600, 600)
    dst = [(150, 0), (0, 0), (15, 150), (135, 150)]
    dst = np.array(dst, dtype = "float32")
    dst[:, 0] += 225
    dst[:, 1] += 300

    # perspective mapping
    M = cv2.getPerspectiveTransform(rect, dst)
    face = cv2.warpPerspective(face, M, size)

    # adjust the landmarks
    new_height, new_width = face.shape[:2]
    for part, detail in marks.items():
        for key, value in detail.items():
            tmp = [value['x'] * width / 100, value['y'] * height / 100, 1]
            res = np.dot(M, tmp)
            marks[part][key]['x'] = res[0] * 100 / res[2] / new_width
            marks[part][key]['y'] = res[1] * 100 / res[2] / new_height

    return face, marks