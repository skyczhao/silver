# -*- coding: utf-8 -*-
# $File: main.py
# $Date: Oct 20 11:50 2014

__author__ = 'tobin'

import os
import cv2
import road
import split
import front

def get_road(image):
    # get road region
    road_region = road.get_road_region(image)
    # split road region
    road_split = split.split_available_road(image, road_region)
    # get the front road
    road_front = front.get_front_road(road_split)

    return road_front

if __name__ == "__main__":
    print "Please use me in function!"
