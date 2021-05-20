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
    return cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    # return cv.cvtColor(image, cv.COLOR_RGB2GRAY)


# OTSU大津法
def threshold(blurred):
    ret, binary1 = cv.threshold(blurred, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    retval, binary2 = cv.threshold(blurred, 127, 255, cv.THRESH_BINARY_INV)
    print("threshold value: %s" % ret)
    return binary1, binary2


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
        return ndimage.rotate(img, rotate_angle), ndimage.rotate(image, rotate_angle)


# def getHProjection(image):
#     hProjection = np.zeros(image.shape, np.uint8)
#     (h, w) = image.shape
#     h_ = [0] * h
#     for y in range(h):
#         for x in range(w):
#             if image[y, x] == 255:
#                 h_[y] += 1
#
#     for y in range(h):
#         for x in range(h_[y]):
#             hProjection[y, x] = 255
#     cv.imshow('hProjection2', hProjection)
#
#     return h_
def getHProjection(image):
    hProjection = np.zeros(image.shape, np.uint8)
    # 图像高与宽
    (h, w) = image.shape
    # 长度与图像高度一致的数组
    h_ = [0] * h
    # 循环统计每一行白色像素的个数
    for y in range(h):
        for x in range(w):
            if image[y, x] == 255:
                h_[y] += 1
    # 绘制水平投影图像
    for y in range(h):
        for x in range(h_[y]):
            hProjection[y, x] = 255
    cv.imshow('hProjection2', hProjection)

    return h_

def getVProjection(image):
    vProjection = np.zeros(image.shape, np.uint8)
    (h, w) = image.shape
    w_ = [0] * w
    for x in range(w):
        for y in range(h):
            if image[y, x] == 255:
                w_[x] += 1
    for x in range(w):
        for y in range(h - w_[x], h):
            vProjection[y, x] = 255
    cv.imshow('vProjection', vProjection)
    return w_


img = cv.imread("houghTest5.png")
# img = cv.imread("houghTest5.png")
gray = gray(img)
blurred = blur(gray)
binary1, binary2 = threshold(gray)
# binary1, binary2 = threshold(blurred)
rotated_image, rotated_bi = hough(binary1)
(h, w) = binary2.shape
Position = []
# H = getHProjection(binary)
H = getHProjection(binary2)
start = 0
H_start = []
H_end = []
for i in range(len(H)):
    if H[i] > 0 and start == 0:
        H_start.append(i)
        start = 1
    if H[i] <= 0 and start == 1:
        H_end.append(i)
        start = 0

for i in range(len(H_start)):
    cropImg = binary2[H_start[i]:H_end[i], 0:w]
    # cropImg = rotated_bi[H_start[i]:H_end[i], 0:w]
    cv.imshow("cropImg", cropImg)
    W = getVProjection(cropImg)
    Wstart = 0
    Wend = 0
    W_start = 0
    W_end = 0
    for j in range(len(W)):
        if W[j] > 0 and Wstart == 0:
            W_start = j
            Wstart = 1
            Wend = 0
        if W[j] <= 0 and Wstart == 1:
            W_end = j
            Wstart = 0
            Wend = 1
        if Wend == 1:
            Position.append([W_start, H_start[i], W_end, H_end[i]])
            Wend = 0

for m in range(len(Position)):
    cv.rectangle(rotated_image, (Position[m][0], Position[m][1]), (Position[m][2], Position[m][3]), (0, 229, 238), 1)
cv.imshow('rotated_image', rotated_image)

# cv.imshow("img", img)
# cv.imshow("gray", gray)
# cv.imshow("blurred", blurred)
# cv.imshow("binary", binary)
# cv.imshow("hough", rotated_image)
cv.waitKey(0)
