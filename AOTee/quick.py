__author__ = 'tobin'

import numpy as np

import cv2

from read import aoteeRead
from otee.eye import eyeMatch
from otee.face import faceMatch
from otee.nose import random_nose
from otee.mouth import random_mouth
from write import maskadd


def generate(location):
    """ generate a comic face according to input image location

    :param location:
    :return:
        comicFinal
    """

    # read image
    result = aoteeRead(location)
    image, attribute = result

    # OTee
    # face
    result = faceMatch(image, attribute, "/home/tobin/Documents/WOTee/media/parts/2")
    face_region, face_comic, face_comic_name = result
    # eye
    result = eyeMatch(image, attribute, "/home/tobin/Documents/WOTee/media/parts/4")
    eye_region, eye_comic, eye_comic_name = result
    # nose & mouth
    mouth_comic = random_mouth("/home/tobin/Documents/WOTee/media/parts/5")
    nose_comic = random_nose("/home/tobin/Documents/WOTee/media/data/nose")

    # generate the final result
    mix_eye = maskadd(face_comic[:, :, :3], eye_comic[:, :, :3], eye_comic[:, :, 3])
    mix_eye_alpha = cv2.bitwise_or(face_comic[:, :, 3], eye_comic[:, :, 3])

    mix_eye_nose = maskadd(mix_eye, nose_comic[:, :, :3], nose_comic[:, :, 3])
    mix_eye_nose_alpha = cv2.bitwise_or(mix_eye_alpha, nose_comic[:, :, 3])

    mix_eye_nose_mouth = maskadd(mix_eye_nose, mouth_comic[:, :, :3], mouth_comic[:, :, 3])
    mix_eye_nose_mouth_alpha = cv2.bitwise_or(mix_eye_nose_alpha, mouth_comic[:, :, 3])

    final = np.dstack([mix_eye_nose_mouth, mix_eye_nose_mouth_alpha])

    return final
