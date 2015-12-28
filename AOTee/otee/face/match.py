# -*- coding: utf-8 -*-
# $File: match.py
# $Date: May 7th. 17:00, 2015.

__author__ = 'tobin'

import os
import re
import cv2
import numpy as np

from detect import get_face_region


def faceMatch(image, attribute, db_path):
    """ match suitable comic face

    :param image:
    :param attribute:
    :param db_path:
    :return:
    """

    # use face region as face feature directly
    feature = get_face_region(image)

    # variables
    maxMatch = 0
    comicFace = None
    comicFaceName = None
    # walk through database path
    ACCEPT_IMAGE_TYPE = re.compile(r".*\.(png|jpg)\Z", re.IGNORECASE)
    for path, subpaths, files in os.walk(db_path):
        for name in files:
            # check suitable file type
            if ACCEPT_IMAGE_TYPE.match(name):
                face_path = os.path.join(db_path, name)

                face_comic = cv2.imread(face_path, cv2.CV_LOAD_IMAGE_UNCHANGED)
                # resize to fixed size
                face_comic = cv2.resize(face_comic, (600, 600))

                # calculate the similarity
                alpha = face_comic[:, :, 3] # alpha as feature
                mask = np.ones(face_comic.shape[:2], np.uint8) * 255
                common = cv2.bitwise_and(feature, alpha, mask=mask)
                number = cv2.countNonZero(common)

                # select the max common face
                if number > maxMatch:
                    maxMatch = number
                    comicFace = face_comic
                    comicFaceName = name

    # check None
    if comicFace is None:
        return None

    # return result
    return feature, comicFace, comicFaceName