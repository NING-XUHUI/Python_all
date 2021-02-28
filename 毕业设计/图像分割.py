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
def threshold(blurred, gradient):
    blurred = cv.GaussianBlur(gradient, (9, 9), 0)
    ret, binary = cv.threshold(blurred, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    print("threshold value: %s" % ret)
    return binary


# 高斯滤波去噪
def blur(gray):
    return cv.GaussianBlur(gray, (9, 9), 0)


def Sobel_Gradient(blurred):
    gradX = cv.Sobel(blurred, ddepth=cv.CV_32F, dx=1, dy=0)
    gradY = cv.Sobel(blurred, ddepth=cv.CV_32F, dx=0, dy=1)
    gradient = cv.subtract(gradX, gradY)
    gradient = cv.convertScaleAbs(gradient)
    return gradX, gradY, gradient


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


def image_morphology(binary):
    # 椭圆核函数
    kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (25, 25))
    # 执行图像形态学
    closed = cv.morphologyEx(binary, cv.MORPH_CLOSE, kernel)
    closed = cv.erode(closed, None, iterations=4)
    closed = cv.dilate(closed, None, iterations=4)

    return closed


def findcnts_and_box_point(closed):
    (cnts, n) = cv.findContours(closed.copy(), cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
    c = sorted(cnts, key=cv.contourArea, reverse=True)[0]
    rect = cv.minAreaRect(c)
    box = np.int0(cv.boxPoints(rect))

    return box


def drawcnts_and_cut(original_img, box):
    draw_img = cv.drawContours(original_img.copy(), [box], -1, (0, 0, 255), 3)

    Xs = [i[0] for i in box]
    Ys = [i[1] for i in box]
    x1 = min(Xs)
    x2 = max(Xs)
    y1 = min(Ys)
    y2 = max(Ys)
    hight = y2 - y1
    width = x2 - x1
    crop_img = original_img[y1:y1 + hight, x1:x1 + width]

    return draw_img, crop_img


img = cv.imread("houghTest3.png")
gray = gray(img)
blurred = blur(gray)
gradX, gradY, gradient = Sobel_Gradient(blurred)
binary = threshold(blurred, gradient)
rotated_img, rotated_bi = hough(binary)
closed = image_morphology(rotated_bi)
box = findcnts_and_box_point(closed)
draw_img, crop_img = drawcnts_and_cut(rotated_img, box)

cv.imshow("img", img)
# cv.imshow("gray", gray)
# cv.imshow("blurred", blurred)
# cv.imshow("binary", binary)
cv.imshow("hough", rotated_bi)
# cv.imshow("draw_img", draw_img)
# cv.imshow("crop_image", crop_img)
cv.waitKey(0)
