import cv2
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

suanzi_x = np.array([[-1, 0, 1],
                     [-1, 0, 1],
                     [-1, 0, 1]])
suanzi_y = np.array([[-1, -1, -1],
                     [0, 0, 0],
                     [1, 1, 1]])

image = cv2.imread("../../TEST.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image_x = np.uint8(signal.convolve2d(image, suanzi_x))
image_y = np.uint8(signal.convolve2d(image, suanzi_y))

image_xy = np.sqrt(image_x ** 2 + image_y ** 2)
image_xy = np.uint8((255.0 / image_xy.max()) * image_xy)
cv2.imshow("x", image_x)
cv2.imshow("y", image_y)
cv2.imshow("xy", image_xy)
cv2.waitKey(0)
