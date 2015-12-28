# -*- coding: utf-8 -*-

__author__ = 'tobin'

# import cv2
# import numpy as np
#
# road = cv2.imread('../test/road_perspective.jpg')
# img = cv2.cvtColor(road, cv2.COLOR_RGB2GRAY)
#
# size = np.size(img)
# skel = np.zeros(img.shape,np.uint8)
#
# ret,img = cv2.threshold(img,127,255,0)
# element = cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))
# done = False
#
# while( not done):
#     eroded = cv2.erode(img,element)
#     temp = cv2.dilate(eroded,element)
#     temp = cv2.subtract(img,temp)
#     skel = cv2.bitwise_or(skel,temp)
#     img = eroded.copy()
#
#     zeros = size - cv2.countNonZero(img)
#     if zeros==size:
#         done = True
#
# cv2.imshow("skel",skel)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

from skimage import morphology
import cv2
import numpy as np

# im = cv2.imread('horse.png')
im = cv2.imread('../test/road_perspective.jpg')
im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
ori = im.copy()
_, im = cv2.threshold(im, 127, 255, cv2.THRESH_BINARY_INV)
im = cv2.threshold(im, 0, 255, cv2.THRESH_OTSU)[1]
im = morphology.skeletonize(im > 0)
im = im.astype(np.uint8)*255
# cv2.imwrite("dst.png", im)

im = np.where(im > 0, 127, 0).astype('uint8')
ori = cv2.bitwise_or(ori, im)
cv2.imshow('origin', ori)
cv2.imshow("skel", im)
cv2.waitKey(0)
cv2.destroyAllWindows()