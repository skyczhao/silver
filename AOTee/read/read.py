# -*- coding: utf-8 -*-
# $File: read.py
# $Date: May, 7. 12:00, 2015.

__author__ = 'tobin'

import cv2
import detect
import normal


def aoteeRead(path):
    """ read face and detect it from path

    :param path:
    :return:
        face:
        attribute:
    """

    # detect attribute from path
    attribute = detect.detect(path)
    if not attribute:
        return None

    # unpack attribute
    gender, age, race, smiling, landmarks = attribute
    # read face from path
    face = cv2.imread(path)

    # normalize image and landmarks
    face, landmarks = normal.normalize(face, landmarks)

    # return result
    return face, (gender, age, race, smiling, landmarks)