__author__ = 'tobin'

import cv2
import numpy as np

def run():
    path = '../data/'
    img_name = 'frame0008.jpg'
    img_path = path + img_name

    img = cv2.imread(img_path)

    # engine cover
    # reference points
    # h, w = img.shape[:2]
    # img = cv2.resize(img, (w/5, h/5))
    rect = [(400, 585), (666, 597), (584, 556), (420, 550)]
    rect = np.array(rect, dtype = "float32")
    for row in rect:
        cv2.circle(img, tuple(row), 3, (0, 0, 255), -1)

    # destination points
    # =====
    # img_dst = cv2.imread('./car_reference.jpg')
    # dst = [(487, 180), (583, 180), (572, 136), (498, 136)]
    # dst = np.array(dst, dtype = "float32")
    # for row in dst:
    #     cv2.circle(img_dst, tuple(row), 3, (0, 255, 0), -1)

    # dst /= 10
    # h, w = img_dst.shape[:2]
    # dst[:, 0] += (w / 2)
    # dst[:, 1] += (h - 20)
    # =====
    # img_dst = cv2.imread('./car_camera_result.jpg')
    # dst = [(487, 180), (583, 180), (572, 136), (498, 136)]
    # dst = np.array(dst, dtype = "float32")
    # for row in dst:
    #     cv2.circle(img_dst, tuple(row), 3, (0, 255, 0), -1)

    # dst /= 10
    # h, w = img_dst.shape[:2]
    # dst[:, 0] += (w / 2)
    # dst[:, 1] += (h - 20)
    # =====
    dst = [(0, 44), (96, 44), (85, 0), (11, 0)]
    dst = np.array(dst, dtype = "float32")
    dst /= 5
    dst[:, 0] += (1024 - 96)
    dst[:, 1] += (2048 - 44)
    print dst

    # w, h = dst[1]
    w, h = 2048, 2048
    M = cv2.getPerspectiveTransform(rect, dst)
    warped = cv2.warpPerspective(img, M, (w, h))

    warped = cv2.resize(warped, (600, 600))

    cv2.imshow(img_name, img)
    cv2.imshow(img_name + ' warp', warped) 
    # cv2.imshow('img_dst', img_dst)
    cv2.waitKey(0)

if __name__ == "__main__":
    run()

    # cv2.circle(img, (110, 347), 3, (0, 255, 0), -1)
    # cv2.circle(img, (800, 396), 3, (0, 255, 0), -1)
    # cv2.circle(img, (769, 384), 3, (0, 255, 0), -1)
    # cv2.circle(img, (156, 335), 3, (0, 255, 0), -1)
