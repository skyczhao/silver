__author__ = 'tobin'

import os
import random
import cv2
import numpy as np


def get_nose_region(image, landmarks):
    # TODO: wait to finish get nose region function
    """ get nose region

    :param image:
    :param landmarks:
    :return:
        noseRegion
    """

    # get image shape
    height, width = image.shape[:2]

    nose_marks = landmarks["nose"]


def random_nose(dbPath):
    """ select nose from database path randomly

    :param dbPath:
    :return:
        comicNose
    """

    # walk through the database path
    yield_walk = os.walk(dbPath)
    for files in yield_walk:
        files = files[2]

    files.sort()
    # random select
    length = len(files)
    ridx = random.randint(1, length)
    nose_name = files[ridx - 1]

    # read and process
    nose_path = dbPath + '/' + nose_name
    nose = cv2.imread(nose_path, cv2.CV_LOAD_IMAGE_UNCHANGED)
    # process
    # nose[:, :, 3] *= 0.85
    nose = cv2.copyMakeBorder(nose, 300, 180, 240, 240, cv2.BORDER_CONSTANT, 0)

    return nose
