import cv2 as cv
import numpy as np
import pybm3d
from skimage.io import imread
import skimage
noise_std_dev = 40
img = imread("../TEST.jpg")
noise = np.random.normal(scale=noise_std_dev,
                         size=img.shape).astype(img.dtype)

noisy_img = img + noise

out = pybm3d.bm3d.bm3d(noisy_img, noise_std_dev)
cv.imshow("out", out)
cv.imshow("img", img)
cv.waitKey(0)