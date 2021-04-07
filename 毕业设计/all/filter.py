import cv2 as cv
import numpy as np

img = cv.imread("../TEST.jpg")
img_mean = cv.blur(img, (5, 5))

