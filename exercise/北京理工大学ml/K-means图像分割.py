
# -*- coding:utf-8 -*-

"""
图像分割：
    利用图像的灰度，颜色，纹理，形状等特征，把图像氛围若干个互不重叠的区域，并使这些特征在
同一区域内呈现相似性，在不同区域之间存在明显差异性，然后就可以将分割的图像中具有独特性质的
区域提取出来用于不同的研究。
"""
import numpy as np
import PIL.Image as image
from sklearn.cluster import KMeans


def loadData(filePath):
    f = open(filePath, 'rb')
    data = []
    img = image.open(f)
    m, n = img.size
    for i in range(m):
        for j in range(n):
            x, y, z = img.getpixel((i, j))
            data.append([x / 256.0, y / 256.0, z / 256.0])
    f.close()
    return np.mat(data), m, n


imgData, row, col = loadData('aaa.JPG')
label = KMeans(n_clusters=5).fit_predict(imgData)

label = label.reshape([row, col])
pic_new = image.new("L", (row, col))
for i in range(row):
    for j in range(col):
        pic_new.putpixel((i, j), int(256 / (label[i][j] + 1)))
pic_new.save("bbb.jpg", "JPEG")
