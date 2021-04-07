import numpy as np
import cv2

image = cv2.imread("../../TEST.jpg")

image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# X方向梯度
sobelX = cv2.Sobel(image, cv2.CV_64F, 1, 0)
sobelX = np.uint8(np.absolute(sobelX))
# Y方向梯度
sobelY = cv2.Sobel(image, cv2.CV_64F, 0, 1)
sobelY = np.uint8(np.absolute(sobelY))

sobelCombined = cv2.bitwise_or(sobelX, sobelY)
cv2.imshow("sobelX", sobelX)
cv2.imshow("sobelY", sobelY)
cv2.imshow("combined", sobelCombined)
cv2.waitKey(0)
