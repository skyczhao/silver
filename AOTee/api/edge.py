# -*- coding: utf-8 -*-
# $File: edge.py
# $Date: Apr 1, 10:40, 2015.

__author__ = 'tobin'

import cv2


def get_canny_edge(image):
    """ canny edge detection

    :param image:
    :return:
        edge: edge graph
    """
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edge = cv2.Canny(gray, 500, 1000, apertureSize=5)
    return edge
