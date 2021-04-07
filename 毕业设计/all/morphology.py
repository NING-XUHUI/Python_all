import cv2 as cv
import numpy as np
img = cv.imread("../TEST.jpg", 0)
# 使用getStructuringElement定义结构元素，shape为结构元素的形状，0表示矩形，1表示十字交叉形，2表示椭圆形，，ksize表示结构元素的大小
# anchor为原点位置，默认值为（-1，-1）表示原点为结构元素的中心点
k = cv.getStructuringElement(shape=1, ksize=(3, 3), anchor=(-1, -1))
# k = np.ones((3, 3), np.uint8)也可以定义一个结构元素
# erode函数实现腐蚀运算，dilate函数表示膨胀运算
erosion = cv.erode(src=img, kernel=k, iterations=1)
cv.imshow("Eroded Image", erosion)

dilation = cv.dilate(img, k, iterations=1)
cv.imshow("Dilated Image", dilation)
opening = cv.morphologyEx(src=img, op=cv.MORPH_OPEN, kernel=k)
closing = cv.morphologyEx(src=img, op=cv.MORPH_CLOSE, kernel=k)
cv.imshow("Opening Image", opening)
cv.imshow("Closing Image", closing)
cv.waitKey(0)


