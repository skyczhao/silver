# -*- coding: utf-8 -*-
# $File: hair.py
# $Date: Apr 3, 13:30, 2015.

__author__ = 'tobin'

import os
import numpy as np

import cv2

from aotee.api.grid import get_grid_feature


def match_hair(hairRegion, dbPath):
    """ match suitable comic hair

    :param hairRegion:
    :param dbPath:
    :return:
        comicHair
    """

    # use hair region to calculate feature
    feature = get_grid_feature(hairRegion, 4)

    # walk through the database path
    yield_walk = os.walk(dbPath)
    for files in yield_walk:
        files = files[2]

    # select the minimum difference hair
    minDiff = 16
    comicHair = 0
    for hair_name in files:
        hair_path = dbPath + '/' + hair_name

        # read hair
        hair = cv2.imread(hair_path, cv2.CV_LOAD_IMAGE_UNCHANGED)
        hair = cv2.resize(hair, (600, 600))

        # get hair color
        black = cv2.inRange(hair, (0, 0, 0, 255), (30, 30, 30, 255))

        # get feature
        hairFeature = get_grid_feature(black, 4)
        # compare
        diff = hairFeature - feature
        refer = np.sum(np.abs(diff))

        if refer < minDiff:
            minDiff = refer
            comicHair = hair

    return comicHair