__author__ = 'tobin'

import os
import random
import cv2


def random_mouth(dbPath):
    """ select mouth from database randomly

    :param dbPath:
    :return:
        comicMouth
    """

    # walk through the database path
    yield_walk = os.walk(dbPath)
    for files in yield_walk:
        files = files[2]

    files.sort()
    # random select
    length = len(files)
    ridx = random.randint(1, length)
    mouth_name = files[ridx - 1]

    # read and process
    mouth_path = dbPath + '/' + mouth_name
    mouth = cv2.imread(mouth_path, cv2.CV_LOAD_IMAGE_UNCHANGED)
    # process
    mouth = cv2.copyMakeBorder(mouth, 380, 100, 240, 240, cv2.BORDER_CONSTANT, 0)

    return mouth