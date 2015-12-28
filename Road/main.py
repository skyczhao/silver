# -*- coding: utf-8 -*-
# $File: main.py
# $Date: Jan 8 21:20 2014

import os
import numpy as np
import cv2

from get import main
from map import map
from marching import skeleton

path = './data/'

yield_walk = os.walk(path)
for files in yield_walk:
    files = files[2]

# for img_name in files:
#     print img_name + ': processing...'
#
#     img_path = path + img_name

img_path = './data/frame0008.jpg'
image = cv2.imread(img_path)
cv2.imshow('image', image)

warped = map.get_perspective(image)
cv2.imshow('warped', warped)

road = main.get_road(warped)
cv2.imshow('road', road)

skele = skeleton.get_skeleton(road)
cv2.imshow('skele', skele)

# road_invert = np.where(road > 0, 0, 255).astype('uint8')
# cv2.imwrite('./test/road_perspective.jpg', road_invert)

merge = cv2.bitwise_xor(road, skele)
cv2.imshow('merge', merge)

origin = map.invert_perspective(merge)
cv2.imshow('origin', origin)

cv2.waitKey(0)
cv2.destroyAllWindows()
