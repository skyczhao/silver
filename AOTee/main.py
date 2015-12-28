__author__ = 'tobin'

import cv2
import numpy as np

from read import aoteeRead
from otee.eye import eyeMatch
from otee.face import faceMatch
from otee.nose import random_nose
from otee.mouth import random_mouth
from write import maskadd

image_path = "/home/tobin/Documents/WOTee/media/raw/04002.jpg"
# image_path = "/home/tobin/Documents/WOTee/media/data/hair/pic_s1_0.png"

result = aoteeRead(image_path)
if result is None:
    print "error face"
else:
    print "detect finish"
    image, attribute = result

    result = eyeMatch(image, attribute, "/home/tobin/Documents/WOTee/media/parts/4")
    print "eye finish"
    eye_region, eye_comic, eye_comic_name = result

    result = faceMatch(image, attribute, "/home/tobin/Documents/WOTee/media/parts/2")
    print "face finish"
    face_region, face_comic, face_comic_name = result

    nose_comic = random_nose("/home/tobin/Documents/WOTee/media/data/nose")

    mouth_comic = random_mouth("/home/tobin/Documents/WOTee/media/parts/5")

    # generate the final result
    mix_eye = maskadd(face_comic[:, :, :3], eye_comic[:, :, :3], eye_comic[:, :, 3])
    mix_eye_alpha = cv2.bitwise_or(face_comic[:, :, 3], eye_comic[:, :, 3])

    mix_eye_nose = maskadd(mix_eye, nose_comic[:, :, :3], nose_comic[:, :, 3])
    mix_eye_nose_alpha = cv2.bitwise_or(mix_eye_alpha, nose_comic[:, :, 3])

    mix_eye_nose_mouth = maskadd(mix_eye_nose, mouth_comic[:, :, :3], mouth_comic[:, :, 3])
    mix_eye_nose_mouth_alpha = cv2.bitwise_or(mix_eye_nose_alpha, mouth_comic[:, :, 3])

    final = np.dstack([mix_eye_nose_mouth, mix_eye_nose_mouth_alpha])
    cv2.imshow('final', final)
    cv2.waitKey(0)
