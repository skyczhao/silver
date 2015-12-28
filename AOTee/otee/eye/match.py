# -*- coding: utf-8 -*-
# $File: match.py
# $Date: May 7th, 13:30, 2015.

__author__ = 'tobin'

import os
import re
import cv2

from api.edge import get_canny_edge

from eye import get_eye_region
from pretreatment import myotee_process


def eyeMatch(image, attribute, db_path):
    """ match a suitable comic eye from specified database path

    :param image:
    :param attribute:
    :param db_path:
    :return:
    """

    # unpack attribute
    gender, age, race, smiling, landmarks = attribute

    # detect edge as feature
    edge = get_canny_edge(image)
    region = get_eye_region(image, landmarks)
    feature = cv2.bitwise_and(edge, edge, mask=region)

    # variables ready for match
    maxMatch = 0
    comicEye = None
    comicEyeName = None
    # walk through database path
    ACCEPT_IMAGE_TYPE = re.compile(r".*\.(png|jpg)\Z", re.IGNORECASE)
    for path, subpaths, files in os.walk(db_path):
        for name in files:
            # check suitable file type
            if ACCEPT_IMAGE_TYPE.match(name):
                eye_path = os.path.join(db_path, name)

                # read eye and get feature
                eye_comic = cv2.imread(eye_path, cv2.CV_LOAD_IMAGE_UNCHANGED)
                eye_comic = myotee_process(eye_comic)
                alpha = eye_comic[:, :, 3]

                # use the same feature detection
                eye_feature = get_canny_edge(eye_comic)

                # compare
                cover = cv2.bitwise_and(feature, eye_feature, mask=alpha)
                number = cv2.countNonZero(cover)
                # select the max fitting
                if number > maxMatch:
                    maxMatch = number
                    comicEye = eye_comic
                    comicEyeName = name

    # avoid None type
    if comicEye is None:
        return None

    # return result
    return region, comicEye, comicEyeName