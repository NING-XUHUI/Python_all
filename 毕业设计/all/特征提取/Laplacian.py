import numpy as np
import cv2 
image = cv2.imread("../../TEST.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# 拉普拉斯边缘检测
lap = cv2.Laplacian(image, cv2.CV_64F)
lap = np.uint8(np.absolute(lap))
cv2.imshow("lap", lap)
cv2.waitKey(0)