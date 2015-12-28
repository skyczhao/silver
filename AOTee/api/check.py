# -*- coding: utf-8 -*-
# $File: check.py
# $Date: Mar 26, 16:20, 2015.

__author__ = 'tobin'

import cv2


def check_landmarks(image, landmarks):
    """ check the landmarks position

    :param image:
    :param landmarks:
    :return:
        face: mark with landmarks
    """

    # copy image to process
    face = image.copy()
    height, width = face.shape[:2]

    # draw right eyebrow
    right_eyebrow = landmarks["right_eyebrow"]
    for key, value in right_eyebrow.items():
        value["x"] = value["x"] * width / 100
        value["y"] = value["y"] * height / 100
        cv2.circle(face, (int(value["x"]), int(value["y"])), 2, (0, 255, 255), -1)

    # draw right eye
    right_eye = landmarks["right_eye"]
    for key, value in right_eye.items():
        value["x"] = value["x"] * width / 100
        value["y"] = value["y"] * height / 100
        cv2.circle(face, (int(value["x"]), int(value["y"])), 2, (0, 0, 255), -1)

    # draw left eyebrow
    left_eyebrow = landmarks["left_eyebrow"]
    for key, value in left_eyebrow.items():
        value["x"] = value["x"] * width / 100
        value["y"] = value["y"] * height / 100
        cv2.circle(face, (int(value["x"]), int(value["y"])), 2, (255, 255, 0), -1)

    # draw left eye
    left_eye = landmarks["left_eye"]
    for key, value in left_eye.items():
        value["x"] = value["x"] * width / 100
        value["y"] = value["y"] * height / 100
        cv2.circle(face, (int(value["x"]), int(value["y"])), 2, (0, 255, 0), -1)

    # draw nose
    nose = landmarks["nose"]
    for key, value in nose.items():
        value["x"] = value["x"] * width / 100
        value["y"] = value["y"] * height / 100
        cv2.circle(face, (int(value["x"]), int(value["y"])), 2, (255, 0, 0), -1)

    # draw mouth
    mouth = landmarks["mouth"]
    for key, value in mouth.items():
        value["x"] = value["x"] * width / 100
        value["y"] = value["y"] * height / 100
        cv2.circle(face, (int(value["x"]), int(value["y"])), 2, (255, 0, 255), -1)

    # draw contour
    contour = landmarks["contour"]
    for key, value in contour.items():
        value["x"] = value["x"] * width / 100
        value["y"] = value["y"] * height / 100
        cv2.circle(face, (int(value["x"]), int(value["y"])), 2, (255, 255, 255), -1)

    return face