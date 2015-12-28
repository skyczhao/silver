# -*- coding: utf-8 -*-
# $File: split.py
# $Date: Jan 4 16:50 2015

__author__ = 'tobin'

import numpy as np
import cv2

K_SIZE = 8
kernel = np.ones((K_SIZE, K_SIZE), np.uint8)

mark_lower_bound = (29, 100, 100)
mark_upper_bound = (31, 180, 180)

def split_available_road(image, road_region):
    # detect marks using hsv color space
    image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    mark_region = cv2.inRange(image_hsv, mark_lower_bound, mark_upper_bound)

    # to get a smooth mark region
    mark_region = cv2.dilate(mark_region, kernel)
    mark_region = cv2.erode(mark_region, kernel)

    # expand the marks
    mark_edges = cv2.Canny(mark_region, 50, 150, apertureSize=3)
    mark_lines = cv2.HoughLines(mark_edges, 1, np.pi/180, 35)

    # draw on the road region
    road_split = road_region.copy()
    if mark_lines is not None:
        for rho, theta in mark_lines[0]:
            a = np.cos(theta)
            b = np.sin(theta)
            x0 = a * rho
            y0 = b * rho
            x1 = int(x0 + 1000 * (-b))
            y1 = int(y0 + 1000 * (a))
            x2 = int(x0 - 1000 * (-b))
            y2 = int(y0 - 1000 * (a))
            cv2.line(road_split, (x1, y1), (x2, y2), 0, 2)
    return road_split