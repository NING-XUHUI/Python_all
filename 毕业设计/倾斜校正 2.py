#!/usr/bin/env python
# coding=utf-8

import os


import cv2 as cv
import numpy as np
import math
import random
from scipy import misc, ndimage
import matplotlib.pyplot as plt
from scipy.stats import mode


def get_img_rot_broa(img, degree, filled_color=-1):
    """
    Desciption:
            Get img rotated a certain degree,
        and use some color to fill 4 corners of the new img.
    """

    # 获取旋转后4角的填充色
    if filled_color == -1:
        filled_color = mode([img[0, 0], img[0, -1],
                             img[-1, 0], img[-1, -1]]).mode[0]
    if np.array(filled_color).shape[0] == 2:
        if isinstance(filled_color, int):
            filled_color = (filled_color, filled_color, filled_color)
    else:
        filled_color = tuple([int(i) for i in filled_color])

    height, width = img.shape[:2]

    # 旋转后的尺寸
    height_new = int(width * math.fabs(math.sin(math.radians(degree))) +
                     height * math.fabs(math.cos(math.radians(degree))))
    width_new = int(height * math.fabs(math.sin(math.radians(degree))) +
                    width * math.fabs(math.cos(math.radians(degree))))

    mat_rotation = cv.getRotationMatrix2D((width / 2, height / 2), degree, 1)

    mat_rotation[0, 2] += (width_new - width) / 2
    mat_rotation[1, 2] += (height_new - height) / 2

    # Pay attention to the type of elements of filler_color, which should be
    # the int in pure python, instead of those in numpy.
    img_rotated = cv.warpAffine(img, mat_rotation, (width_new, height_new),
                                 borderValue=filled_color)
    # 填充四个角
    mask = np.zeros((height_new + 2, width_new + 2), np.uint8)
    mask[:] = 0
    seed_points = [(0, 0), (0, height_new - 1), (width_new - 1, 0),
                   (width_new - 1, height_new - 1)]
    for i in seed_points:
        cv.floodFill(img_rotated, mask, i, filled_color)

    return img_rotated


# 灰度图
def gray(image):
    return cv.cvtColor(image, cv.COLOR_RGB2GRAY)


# OTSU大津法
def threshold(blurred):
    ret, binary = cv.threshold(blurred, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    print("threshold value: %s" % ret)
    return binary


# 高斯滤波去噪
def blur(gray):
    return cv.GaussianBlur(gray, (9, 9), 0)


# HOUGH变换
def hough(image):
    edges = cv.Canny(image, 50, 150, apertureSize=3)
    # cv.imshow("edges", edges)
    lines = cv.HoughLines(edges, 1, np.pi / 180, 0)
    for rho, theta in lines[0]:
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a * rho
        y0 = b * rho
        x1 = int(x0 + 1000 * (-b))
        y1 = int(y0 + 1000 * a)
        x2 = int(x0 - 1000 * (-b))
        y2 = int(y0 - 1000 * a)
        if x1 == x2 or y1 == y2:
            continue
        t = float(y2 - y1) / (x2 - x1)
        rotate_angle = math.degrees(math.atan(t))
        if rotate_angle > 45:
            rotate_angle = -90 + rotate_angle
        elif rotate_angle < -45:
            rotate_angle = 90 + rotate_angle
        print("rotate angle : {}".format(rotate_angle))
        return rotate_angle
        #return ndimage.rotate(img, rotate_angle)


img = cv.imread("../SVM/data1/二/6.jpg")

gray = gray(img)
blurred = blur(gray)
binary = threshold(blurred)
rotated_angle = hough(binary)
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
#rotated = cv.cvtColor(ndimage.rotate(img, rotated_angle), cv.COLOR_BGR2RGB)
rotated = get_img_rot_broa(img, rotated_angle)
plt.subplot(1,2,1)
plt.imshow(img)
plt.xticks([])
plt.yticks([])
plt.title("Original Image")
plt.subplot(1,2,2)
rotated = cv.cvtColor(rotated, cv.COLOR_BGR2GRAY)
rotated = cv.GaussianBlur(rotated, (5, 5), 0)
cv.imshow("gray", rotated)
_, rotated = cv.threshold(rotated, 0, 255, cv.THRESH_OTSU | cv.THRESH_BINARY)
rotated = cv.resize(rotated, (32, 32))
plt.imshow(rotated, cmap='binary')
plt.xticks([])
plt.yticks([])
plt.title("Rotated Image")
plt.show()
# cv.imshow("img", img)
# cv.imshow("gray", gray)
# cv.imshow("blurred", blurred)
# cv.imshow("binary", binary)
# cv.imshow("hough", rotated)
# cv.waitKey(0)
