# -*- coding: utf-8 -*-
# $File: front.py
# $Date: Jan 8 20:20 2015

__author__ = 'tobin'

import numpy as np
import cv2

K_SIZE = 4
kernel = np.ones((K_SIZE, K_SIZE), np.uint8)

def get_front_road(available_road):
    # in opencv
    # store height first, and then width
    # the color channel is B-G-R, inverse
    height, width = available_road.shape[:2]

    # get the flood seed position
    seed_width = width / 2
    seed_height = height / 2
    for seed_height in range(height, 0, -1):
        if available_road[seed_height - 1, seed_width - 1] > 0:
            break

    # flood fill
    mask = np.zeros((height + 2, width + 2), np.uint8)
    front_road = available_road.copy()
    # here is the right order of width and height of the seed point
    # must subtract 1 to the real index of image
    cv2.floodFill(front_road, mask, (seed_width - 1, seed_height - 1), 127)

    # post processing
    front_road = np.where(front_road == 127, 255, 0).astype('uint8')
    front_road = cv2.dilate(front_road, kernel)
    front_road = cv2.erode(front_road, kernel)
    front_road = np.where(front_road > 0, 255, 0).astype('uint8')

    return front_road
