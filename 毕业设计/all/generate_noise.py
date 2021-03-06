import cv2 as cv
import random

img = cv.imread("../TEST.jpg")
imgInfo = img.shape
height = imgInfo[0] - 1
width = imgInfo[1] - 1

temp = 10000

for i in range(0, temp):
    if random.randint(1, temp) % 2 == 0:
        img[random.randint(0, height), random.randint(0, width)] = (255, 255, 255)
    if random.randint(1, temp) % 2 != 0:
        img[random.randint(0, height), random.randint(0, width)] = (0, 0, 0)

cv.imshow("asd", img)
cv.imwrite("../noiseTest.jpg", img)
cv.waitKey(0)