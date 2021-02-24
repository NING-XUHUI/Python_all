#!/usr/bin/env python
# coding=utf-8


import cv2 as cv
import numpy as np


# OTSU大津法
# def threshold(image):
#     gray = cv.cvtColor(image, cv.COLOR_RGB2GRAY)
#     ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
#     print("threshold value: %s" % ret)
#     cv.imshow("binary", binary)
#     cv.waitKey(0)


def rotate_bound(image, angle):
    # 获取宽和高
    (h, w) = image.shape[:2]
    (cX, cY) = (w // 2, h // 2)

    # 提取旋转矩阵 sin cos
    M = cv.getRotationMatrix2D((cX, cY), -angle, 1.0)
    cos = np.abs(M[0, 0])
    sin = np.abs(M[0, 1])

    # 计算图像的新边界尺寸
    nW = int((h * sin) + (w * cos))
    nH = h

    # 调整旋转矩阵
    M[0, 2] += (nW / 2) - cX
    M[1, 2] += (nH / 2) - cY

    return cv.warpAffine(image, M, (nW, nH), flags=cv.INTER_CUBIC, borderMode=cv.BORDER_REPLICATE)


def get_minAreaRect(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    gray = cv.bitwise_not(gray)
    thresh = cv.threshold(gray, 0, 255,
                           cv.THRESH_BINARY | cv.THRESH_OTSU)[1]
    coords = np.column_stack(np.where(thresh > 0))
    return cv.minAreaRect(coords)


img = cv.imread("../demo.jpg")
angle = get_minAreaRect(img)[-1]
rotated = rotate_bound(img, angle)

cv.imshow("input", img)
cv.imshow("output", rotated)
cv.waitKey(0)
