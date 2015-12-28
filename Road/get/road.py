# -*- coding: utf-8 -*-
# $File: road.py
# $Date: Jan 4 16:47 2015

__author__ = 'tobin'

import cv2
import numpy as np

road_color = (145, 145, 145)
range = 10

def get_road_region(image):
    road_color_array = np.array(road_color)
    road_region = cv2.inRange(image, road_color_array - range, road_color_array + range)
    return road_region