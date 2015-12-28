# -*- coding: utf-8 -*-

import os
import numpy as np
import cv2

K_SIZE = 150
kernel = np.ones((K_SIZE, K_SIZE), np.uint8)
# kernel[K_SIZE / 2, :] = 1
# kernel[:, K_SIZE / 2] = 1

path = '../data/'

yield_walk = os.walk(path)
for files in yield_walk:
    files = files[2]

for img_name in files:
    print img_name + ': processing...'

    # img_name = 'frame0144.jpg'
    img = cv2.imread(path + img_name)

    # BGR, store blue plane firstly
    road_color = cv2.inRange(img, (130, 130, 130), (170, 170, 170))
    mark_color = cv2.inRange(img, (50, 130, 130), (90, 220, 220))

    # road_color = cv2.erode(road_color, kernel)
    # road_color = cv2.dilate(road_color, kernel)
    # cv2.imshow('er_ro_co', road_color)
    # cv2.imshow('img', img)
    # cv2.waitKey(0)
    # break

    # mark_color = cv2.dilate(mark_color, kernel)

    # detect lines
    edges = cv2.Canny(mark_color, 50, 150, apertureSize=3)
    lines = cv2.HoughLines(edges, 1, np.pi/180, 50)
    # draw lines
    if lines is not None:
        for rho, theta in lines[0]:
            a = np.cos(theta)
            b = np.sin(theta)
            x0 = a * rho
            y0 = b * rho
            x1 = int(x0 + 1000 * (-b))
            y1 = int(y0 + 1000 * (a))
            x2 = int(x0 - 1000 * (-b))
            y2 = int(y0 - 1000 * (a))
            cv2.line(road_color, (x1, y1), (x2, y2), 0, 2)

    # flood fill
    h, w = img.shape[:2]
    mask = np.zeros((h+2, w+2), np.uint8)
    seed_pt = 500, 450
    cv2.floodFill(road_color, mask, seed_pt, 127)

    # road region
    road_region = np.where(road_color == 127, 255, 0).astype('uint8')

    # road
    road = cv2.bitwise_and(img, img, mask=road_region)

    cv2.imshow('origin', img)
    cv2.imshow('road', road)

    cv2.waitKey(0)
    # break