# -*- coding: utf-8 -*-

__author__ = 'tobin'

import math
import numpy as np

def real_position(size, image_pos, camera_para, camera_rot, camera_pos):
    T = position_matrix(camera_pos)
    R = rotation_matrix(camera_rot)
    fx, fy = camera_para
    xp, yp = image_pos
    width, height = size

    # perspective camera point
    xc = (xp - width / 2) / fx
    yc = (yp - height / 2) / fy

    # coordinate transformation point
    zr = 0.915348425339
    xr = xc * zr
    yr = yc * zr

    # Vt = R'Vr
    Vr = np.array([[xr, yr, zr, 1.0]])
    Vr = np.transpose(Vr)
    Vt = np.dot(np.linalg.inv(R), Vr)
    # Vo = T'Vt
    Vo = np.dot(np.linalg.inv(T), Vt)

    xo, yo, zo, _ = tuple(row[0] for row in Vo)
    return (xo, yo, zo)

def inner_parameter(size, image_pos, camera_rot, camera_pos, refer_pos):
    xo, yo, zo = refer_pos
    T = position_matrix(camera_pos)
    R = rotation_matrix(camera_rot)
    xp, yp = image_pos
    width, height = size

    # scene point
    Vo = np.array([[xo, yo, zo, 1.0]])
    Vo = np.transpose(Vo)
    # Vt = TVo
    Vt = np.dot(T, Vo)
    # Vr = RVt
    Vr = np.dot(R, Vt)

    # coordinate transformation point
    xr, yr, zr, _ = tuple(row[0] for row in Vr)

    # perspective camera point
    xc, yc = xr / zr, yr / zr

    # inner parameter
    fx = (xp - width / 2) / xc
    fy = (yp - height / 2) / yc

    return (fx, fy)

def rotation_matrix(camera_rot):
    alpha, beta, gama = camera_rot

    sin_alpha = math.sin(alpha)
    cos_alpha = math.cos(alpha)

    sin_beta = math.sin(beta)
    cos_beta = math.cos(beta)

    sin_gama = math.sin(gama)
    cos_gama = math.cos(gama)

    R = np.array([[cos_beta * cos_gama,
                   cos_beta * sin_gama,
                   -sin_beta,
                   0.0],
                  [sin_alpha * sin_beta * cos_gama - cos_alpha * sin_gama,
                   sin_alpha * sin_beta * sin_gama + cos_alpha * cos_gama,
                   sin_alpha * cos_beta,
                   0.0],
                  [cos_alpha * sin_beta * cos_gama + sin_alpha * sin_gama,
                   cos_alpha * sin_beta * sin_gama - sin_alpha * cos_gama,
                   cos_alpha * cos_beta,
                   0.0],
                  [0.0, 0.0, 0.0, 1.0]])
    return R

def position_matrix(camera_pos):
    x, y, z = camera_pos
    T = np.array([[1.0, 0.0, 0.0, -x],
                  [0.0, 1.0, 0.0, -y],
                  [0.0, 0.0, 1.0, -z],
                  [0.0, 0.0, 0.0, 1.0]])

    return T