import numpy as np
import cv2
import pybm3d
import matplotlib.pyplot as plt
from skimage import measure
from skimage.io import imread
from matplotlib.pyplot import cm
import datetime

img = np.float32(imread('./TEST.jpg'))
img = img[:, :480]
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) / 255
noisy_img = np.float32(imread('./noiseTest.jpg'))
noisy_img = noisy_img[:, :480]
noisy_img = cv2.cvtColor(noisy_img, cv2.COLOR_BGR2GRAY) / 255
# plt.subplot(1,2,1)
# plt.imshow(img, cmap='gray')
# plt.xticks([])
# plt.yticks([])
# plt.title("Original")
# plt.subplot(1,2,2)
# plt.imshow(noisy_img, cmap='gray')
# plt.xticks([])
# plt.yticks([])
# plt.title("Noise")
# plt.show()
psnr = []
times = []
# 高斯滤波
starttime = datetime.datetime.now()
img_Guassian = cv2.GaussianBlur(noisy_img, (5, 5), 0)
endtime = datetime.datetime.now()
times.append((endtime - starttime).seconds)
# 计算处理后图片与原图的 PSNR 值
Guassian_psnr = measure.compare_psnr(img, img_Guassian)
print("PSNR of reconstructed image (Guassian):", Guassian_psnr)
psnr.append(Guassian_psnr)
# BM3D

starttime = datetime.datetime.now()
noise_std_dev = 30
img_bm3d = pybm3d.bm3d.bm3d(noisy_img * 255, noise_std_dev)
endtime = datetime.datetime.now()
# 计算处理后图片与原图的 PSNR 值
bm3d_psnr = measure.compare_psnr(img, img_bm3d / 255)
print("PSNR of reconstructed image (bm3d):", bm3d_psnr)
psnr.append(bm3d_psnr)
times.append((endtime - starttime).seconds)


# NL-means
def nlm(X, N, K, sigma):
    H, W = X.shape
    pad_len = N + K
    Xpad = np.pad(X, pad_len, 'constant', constant_values=0)
    yy = np.zeros(X.shape)
    B = np.zeros([H, W])
    for ny in range(-N, N + 1):
        for nx in range(-N, N + 1):
            ssd = np.zeros((H, W))
            # 根据邻域内像素间相似性确定权重
            for ky in range(-K, K + 1):
                for kx in range(-K, K + 1):
                    ssd += np.square(
                        Xpad[pad_len + ny + ky:H + pad_len + ny + ky, pad_len + nx + kx:W + pad_len + nx + kx] -
                        Xpad[pad_len + ky:H + pad_len + ky,pad_len + kx:W + pad_len + kx])
            ex = np.exp(-ssd / (2 * sigma ** 2))
            B += ex
            yy += ex * Xpad[pad_len + ny:H + pad_len + ny, pad_len + nx:W + pad_len + nx]
    return yy / B


starttime = datetime.datetime.now()
img_nlm = nlm(noisy_img, 10, 4, 0.6)
endtime = datetime.datetime.now()
times.append((endtime - starttime).seconds)
# 计算处理后图片与原图的 PSNR 值
nlm_psnr = measure.compare_psnr(img, img_nlm.astype(np.float32))
print("PSNR of reconstructed image (NL-means):", nlm_psnr)
psnr.append(nlm_psnr)


# 小波阈值
def wavelet(X, levels, lmain):
    def im2wv(img, nLev):
        # pyr array
        pyr = []
        h_mat = np.array([[1, 1, 1, 1],
                          [-1, 1, -1, 1],
                          [-1, -1, 1, 1],
                          [1, -1, -1, 1]])
        for i in range(nLev):
            n, mid = len(img), len(img) // 2
            # split image up for HWT
            a = img[:n:2, :n:2]
            b = img[1:n:2, :n:2]
            c = img[:n:2, 1:n:2]
            d = img[1:n:2, 1:n:2]
            vec = np.array([a, b, c, d])
            # reshape vector to perform mat mult
            D = 1 / 2 * np.dot(h_mat, vec.reshape(4, mid * mid))
            L, H1, H2, H3 = D.reshape([4, mid, mid])
            pyr.append([H1, H2, H3])
            img = L
        pyr.append(L)
        return pyr

    def wv2im(pyr):
        h_mat = np.array([[1, 1, 1, 1],
                          [-1, 1, -1, 1],
                          [-1, -1, 1, 1],
                          [1, -1, -1, 1]])
        h_mat_inv = np.linalg.inv(h_mat)

        L = pyr[-1]
        for [H1, H2, H3] in reversed(pyr[:-1]):
            n, n2 = len(L), len(L) * 2
            vec = np.array([L, H1, H2, H3])

            D = 2 * np.dot(h_mat_inv, vec.reshape(4, n * n))
            a, b, c, d = D.reshape([4, n, n])

            img = np.empty((n2, n2))
            img[:n2:2, :n2:2] = a
            img[1:n2:2, :n2:2] = b
            img[:n2:2, 1:n2:2] = c
            img[1:n2:2, 1:n2:2] = d
            L = img
        return L

    def denoise_coeff(y, lmbda):
        x = np.copy(y)
        x[np.where(y > lmbda / 2.0)] -= lmbda / 2.0
        x[np.where(y < -lmbda / 2.0)] += lmbda / 2.0
        x[np.where(np.logical_and(y > -lmbda / 2.0, y < lmbda / 2.0))] = 0
        return x

    pyr = im2wv(X, levels)
    for i in range(len(pyr) - 1):
        for j in range(2):
            pyr[i][j] = denoise_coeff(pyr[i][j], lmain / (2 ** i))
        pyr[i][2] = denoise_coeff(pyr[i][2], np.sqrt(2) * lmain / (2 ** i))
    im = wv2im(pyr)
    return im


starttime = datetime.datetime.now()
img_wav = wavelet(noisy_img, 5, 0.5)
endtime = datetime.datetime.now()

times.append((endtime - starttime).seconds)
# 计算处理后图片与原图的 PSNR 值
wav_psnr = measure.compare_psnr(img, img_wav.astype(np.float32))
print("PSNR of reconstructed image (Wavelet):", wav_psnr)

# 计算含噪音图片和原图的 PSNR 值
noise_psnr = measure.compare_psnr(img, noisy_img)
print("PSNR of noisy image:", noise_psnr)
psnr.append(wav_psnr)
psnr.append(noise_psnr)

# plt.plot(["Guassian", "BM3D", "NL-means", "wav", "noisy"], psnr)
# plt.ylabel("PSNR")
# plt.title("PSNR FOR EACH ALGORITHM")
# plt.show()
plt.plot(["Guassian", "BM3D", "NL-means", "wav"], times)
plt.ylabel("seconds")
plt.title("SECONDS FOR EACH ALGORITHM")
plt.show()
# 图片存储
# plt.imsave("Guassian.png", img_Guassian, cmap=cm.gray)
# plt.imsave("bm3d.png", img_bm3d / 255, cmap=cm.gray)
# plt.imsave("nlm.png", img_nlm, cmap=cm.gray)
# plt.imsave("wav.png", img_wav, cmap=cm.gray)
# cv2.imshow("Guassian", img_Guassian)
# cv2.imshow("bm3d", img_bm3d / 255)
# cv2.imshow("nlm", img_nlm)
# cv2.imshow("wav", img_wav)
# plt.subplot(2,2,1)
# plt.imshow(img_Guassian, cmap="gray")
# plt.xticks([])
# plt.yticks([])
# plt.title("Guassian")
# plt.subplot(2,2,2)
# plt.imshow(img_bm3d, cmap="gray")
# plt.xticks([])
# plt.yticks([])
# plt.title("BM3D")
# plt.subplot(2,2,3)
# plt.imshow(img_nlm, cmap="gray")
# plt.xticks([])
# plt.yticks([])
# plt.title("NL-means")
# plt.subplot(2,2,4)
# plt.imshow(img_wav, cmap="gray")
# plt.xticks([])
# plt.yticks([])
# plt.title("wav")
# plt.show()

# cv2.waitKey(0)
