# -*- coding: utf-8 -*-
# $File: detect.py
# $Date: Mar 25, 20:00, 2015.

__author__ = 'tobin'

import os
import ConfigParser

# Face++ SDK
from lib.facepp import API
from lib.facepp import File


def detect(path):
    """ detect landmarks of the image

    :param path:

    :return:
        gender
        age
        race
        smiling
        landmarks
    """

    # api configuration
    api_key = "1cfb1862a39c73e4e30b38758101edf1"
    api_secret = "lsyyBYCipU1AKMC4wUTD2l2vkS9p_K_8"

    # using Face++ API to detect key points
    api = API(api_key, api_secret)
    # upload image to Face++ server and return the file attribute
    attribute = api.detection.detect(img=File(path))

    # only interested in face
    face = attribute['face']
    # check face attribute
    if not face:
        return None

    # unpack face attribute
    gender = face[0]['attribute']['gender']['value']
    age = face[0]['attribute']['age']['value']
    race = face[0]['attribute']['race']['value']
    smiling = face[0]['attribute']['smiling']['value']

    # detect more landmarks
    face_id = face[0]['face_id']
    # ask to Face++ server to detect the image which has been uploaded
    result = api.detection.landmark(face_id=face_id, type='83p')
    # unpack result
    landmarks = unpack(result)

    return gender, age, race, smiling, landmarks


def unpack(detect_result):
    """ unpack detect result

    :param detect_result:
    :return:
        {'left_eyebrow': left_eyebrow dict, 'right_eyebrow': right_eyebrow dict,
            'left_eye': left_eye dict, 'right_eye': right_eye dict,
            'nose': nose dict, 'mouth': mouth dict, 'contour': contour dict}
    """

    # just use the first detected face
    landmarks = detect_result['result'][0]['landmark']
    # unpack landmarks to 7 parts
    left_eyebrow = {}
    right_eyebrow = {}
    left_eye = {}
    right_eye = {}
    nose = {}
    mouth = {}
    contour = {}
    for key, value in landmarks.items():
        if "left_eyebrow" in key:
            left_eyebrow[key] = value
        elif "right_eyebrow" in key:
            right_eyebrow[key] = value
        elif "left_eye" in key:
            left_eye[key] = value
        elif "right_eye" in key:
            right_eye[key] = value
        elif "nose" in key:
            nose[key] = value
        elif "mouth" in key:
            mouth[key] = value
        elif "contour" in key:
            contour[key] = value

    # return dict
    return {'left_eyebrow': left_eyebrow, 'right_eyebrow': right_eyebrow,
            'left_eye': left_eye, 'right_eye': right_eye,
            'nose': nose, 'mouth': mouth, 'contour': contour}