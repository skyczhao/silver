# -*- coding: utf-8 -*-

__author__ = 'tobin'

import cv2
import math
import numpy as np

import perspective

image = cv2.imread('../data/frame0008.jpg')

height, width = image.shape[:2]

for i in range(8):
    print str(i) + ' processing...'

# angle
# Rx, Ry, Rz
alpha, beta, gama = (-0.43, 0, 0)
# radian
alpha = np.deg2rad(alpha) # / 180.0 * math.pi
beta = np.deg2rad(beta) # / 180.0 * math.pi
gama = np.deg2rad(gama) # / 180.0 * math.pi
# position
# Px, Py, Pz
x, y = (width / 2.0, height / 2.0)

wrap, center = perspective.rotate((alpha, beta, gama), (x, y), image)
# old, center = perspective.rotate((-alpha, -beta, gama), center, wrap)

cv2.imshow('wrap', wrap)
cv2.waitKey(0)
