import cv2
import numpy as np

image = cv2.imread("../../TEST.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
canny = cv2.Canny(image, 30, 150)
print(canny)
cv2.imshow("canny", canny)
cv2.waitKey(0)