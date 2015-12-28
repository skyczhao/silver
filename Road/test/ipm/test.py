# -*- coding: utf-8 -*-

__author__ = 'tobin'

import cv2
import numpy as np

import camera

camera_pos = (0.150, -0.025, 0.569)
refer_pos = (0.981861, -0.217657, -0.092048)
print refer_pos

# ===== SECTION 10 =====
down_10 = cv2.imread('tilt_head_10.png')
# cv2.imshow('down_10', down_10)

camera_rot = (-1.715, -0.030, -1.552)
image_pos = (500, 682)
height, width = down_10.shape[:2]

camera_para = camera.inner_parameter((width, height), image_pos, camera_rot, camera_pos, refer_pos)
print camera_para

other_pos = (790, 694)
origin_pos = camera.real_position((width, height), other_pos, camera_para, camera_rot, camera_pos)
print origin_pos

cv2.waitKey(0)