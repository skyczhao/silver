# -*- coding: utf-8 -*-

import os
import numpy as np
import cv2

path = './'
img_name = '2.jpg'
img_path = path + img_name

img = cv2.imread(img_path)
height, width = img.shape[:2]
img = cv2.resize(img, (width/5, height/5))

height, width = img.shape[:2]

rect = [(347, 356), (561, 359), (532, 217), (358, 217)]
rect = np.array(rect, dtype = "float32")
for row in rect:
    cv2.circle(img, tuple(row), 3, (0, 255, 0), -1)

dst = [(0, 1), (1, 1), (1, 0), (0, 0)]
dst = np.array(dst, dtype = "float32")
size = 200
dst *= size
dst[:, 0] += (width - size)
dst[:, 1] += (height * 1.5 - size)
M = cv2.getPerspectiveTransform(rect, dst)
warped = cv2.warpPerspective(img, M, (int(width * 1.5), int(height * 1.5)))

cv2.imshow(img_name, img)
cv2.imshow(img_name + ' warped', warped)
cv2.waitKey(0)