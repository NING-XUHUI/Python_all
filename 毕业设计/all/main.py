import cv2 as cv
from matplotlib import pyplot as plt
image = cv.imread("../TEST.jpg")
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
plt.subplot(311)
plt.imshow(gray, "gray")
plt.title("input image")

ret1, th1 = cv.threshold(gray, 0, 255, cv.THRESH_OTSU)
plt.subplot(312)
plt.hist(gray.ravel(), 256)
plt.axvline(x=ret1, color='red', label='ostu')
plt.legend(loc='upper right')
plt.title("Histogram")
plt.xticks([])
plt.yticks([])
plt.subplot(313)
plt.imshow(th1, "gray")
plt.title("output image")
plt.xticks([])
plt.yticks([])
print(ret1)
plt.show()

