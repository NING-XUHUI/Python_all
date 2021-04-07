import cv2 as cv
import numpy as np
import pybm3d
import matplotlib.pyplot as plt
from skimage import metrics
from skimage.io import imread
from matplotlib.pyplot import cm

# 给一张图片随即添加噪声
# img = cv.imread("../TEST.jpg")
# imgInfo = img.shape
# height = imgInfo[0] - 1
# width = imgInfo[0] - 1
#
# temp = 5000
#
# for i in range(0, temp):
#     if random.randint(1, temp) % 2 == 0:
#         img[random.randint(0, height), random.randint(0, width)] = (255, 255, 255)
#     if random.randint(1, temp) % 2 != 0:
#         img[random.randint(0, height), random.randint(0, width)] = (0, 0, 0)

img = np.float32(imread("../TEST.jpg"))
img = cv.cvtColor(img, cv.COLOR_BGR2GRAY) / 255
noisy_img = np.float32(imread("../noiseTest.jpg"))
noisy_img = cv.cvtColor(noisy_img, cv.COLOR_BGR2GRAY) / 255
# 高斯滤波
img_Guassian= cv.GaussianBlur(noisy_img, (5, 5), 0)
# 计算处理后图片与原图的PSNR值
Guassian_psnr = metrics.peak_signal_noise_ratio(img, img_Guassian)
print("PSNR of reconstructed image(Guassian):", Guassian_psnr)
# BM3D
noise_std_dev = 30
img_bm3d = pybm3d.bm3d.bm3d(noisy_img * 255, noise_std_dev)
# PSNR
bm3d_psnr = metrics.peak_signal_noise_ratio(img, img_bm3d / 255)
print("PSNR of reconstructed image(bm3d):", bm3d_psnr)

cv.imshow("original", img)
cv.imshow("noise", noisy_img)
cv.imshow("Guassian", img_Guassian)
cv.imshow("bm3d", img_bm3d)

cv.waitKey(0)

# NL-means





