#!/usr/bin/env python
# coding=utf-8

import os
import cv2 as cv
import numpy as np
import math
import random
from scipy import misc, ndimage


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
    cv.imshow("edges", edges)
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
        return ndimage.rotate(img, rotate_angle)


img = cv.imread("houghTest3.png")
gray = gray(img)
blurred = blur(gray)
binary = threshold(blurred)
rotated = hough(binary)
cv.imshow("img", img)
cv.imshow("gray", gray)
cv.imshow("blurred", blurred)
cv.imshow("binary", binary)
cv.imshow("hough", rotated)
cv.waitKey(0)
