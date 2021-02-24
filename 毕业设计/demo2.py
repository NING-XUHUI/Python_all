import numpy as np
import argparse
import cv2 as cv



image = cv.imread("../hough.png")
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

thresh = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)[1]
coords = np.column_stack(np.where(thresh > 0))
angle = cv.minAreaRect(coords)[-1]

if angle < -45:
    angle = -(90 + angle)
else:
    angle = -angle

(h, w) = image.shape[:2]
center = (w // 2, h // 2)
M = cv.getRotationMatrix2D(center, angle, 1.0)
rotated = cv.warpAffine(image, M, (w, h),
                        flags=cv.INTER_CUBIC, borderMode=cv.BORDER_REPLICATE)
cv.imshow("in", image)
cv.imshow("out", rotated)
cv.waitKey(0)

