__author__ = 'tobin'

import cv2
import numpy as np


def compute_contour(image, landmarks):

    contour = landmarks["contour"]
    height, width = image.shape[:2]

    # marks array
    marks = []
    for i in range(1, 10):
        key = "contour_left" + str(i)
        marks.append([contour[key]["x"], contour[key]["y"]])
    marks.append([contour["contour_chin"]["x"], contour["contour_chin"]["y"]])
    for i in range(9, 0, -1):
        key = "contour_right" + str(i)
        marks.append([contour[key]["x"], contour[key]["y"]])
    marks = np.array(marks)

    # turn the marks to be pixel
    marks[:, 0] = marks[:, 0] * width / 100.0
    marks[:, 1] = marks[:, 1] * width / 100.0
    # move contour to center
    move = marks[9, 0] - width / 2.0
    marks[:, 0] -= move

    # calculate the average position
    dx = (marks[-1:9:-1, 0] - marks[:9, 0]) / 2.0
    y = (marks[-1:9:-1, 1] + marks[:9, 1]) / 2.0
    # reset the marks
    marks[:9, 0] = width / 2.0 - dx
    marks[:9, 1] = y
    marks[-1:9:-1, 0] = width / 2.0 + dx
    marks[-1:9:-1, 1] = y

    # generate the SVG path
    radius = (marks[-1, 0] - marks[0, 0]) / 2.0
    template = "M%f,%f " % tuple(marks[0])
    for i in range(1, 19):
        template += "L%f,%f " % tuple(marks[i])
    template += "A%f,%f 0 1,0 %f,%f z" % (radius, radius, marks[0, 0], marks[0, 1])

    print template
