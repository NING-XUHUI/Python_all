#!/usr/bin/python 
# -*- coding:utf-8 -*-

"""
非负举证矩阵分解是在矩阵中所有元素均
为非负数约束条件之下的矩阵分解方法

基本思想：
    给定一个非负矩阵V，NMF能够找到一个非负
矩阵W和一个非负矩阵H，是的矩阵W和H的乘积近似等于
矩阵V中的值。

W矩阵：基础图像矩阵，相当于从愿矩阵V中抽取出来的特征
H矩阵：系数矩阵

NMF广泛应用于图像分析、文本挖掘和语音处理等领域

矩阵分解优化目标：最小化W矩阵H矩阵的乘积和原始矩阵之间的差别
"""

from numpy.random import RandomState
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_olivetti_faces
from sklearn import decomposition

n_row, n_col = 2, 3
n_components = n_row * n_col
image_shape = (64, 64)

###############################################################################
# Load faces data
dataset = fetch_olivetti_faces(shuffle=True, random_state=RandomState(0))
faces = dataset.data


###############################################################################
def plot_gallery(title, images, n_col=n_col, n_row=n_row):
    plt.figure(figsize=(2. * n_col, 2.26 * n_row))
    plt.suptitle(title, size=16)

    for i, comp in enumerate(images):
        plt.subplot(n_row, n_col, i + 1)
        vmax = max(comp.max(), -comp.min())

        plt.imshow(comp.reshape(image_shape), cmap=plt.cm.gray,
                   interpolation='nearest', vmin=-vmax, vmax=vmax)
        plt.xticks(())
        plt.yticks(())
    plt.subplots_adjust(0.01, 0.05, 0.99, 0.94, 0.04, 0.)


plot_gallery("First centered Olivetti faces", faces[:n_components])
###############################################################################

estimators = [
    ('Eigenfaces - PCA using randomized SVD',
     decomposition.PCA(n_components=6, whiten=True)),

    ('Non-negative components - NMF',
     decomposition.NMF(n_components=6, init='nndsvda', tol=5e-3))
]

###############################################################################

for name, estimator in estimators:
    print("Extracting the top %d %s..." % (n_components, name))
    print(faces.shape)
    estimator.fit(faces)
    components_ = estimator.components_
    plot_gallery(name, components_[:n_components])

plt.show()
