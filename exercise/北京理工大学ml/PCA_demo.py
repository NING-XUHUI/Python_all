#!/usr/bin/python
# -*- coding:utf-8 -*-


from sklearn.datasets import load_iris  # 鸢尾花数据集
import matplotlib.pyplot as plt  # 数据可视化
from sklearn.decomposition import PCA  # 加载PCA算法包

# 加载数据并进行降维

data = load_iris()  # 以字典形式加载鸢尾花数据集

y = data.target  # 使用y表示数据集的标签
x = data.data  # 使用x表示数据集的属性数据
pca = PCA(n_components=2)  # 加载PCA算法，设置降维后主成分数目为2
reduced_X = pca.fit_transform(x);  # 对原始数据进行降维，保存
red_x, red_y = [], []
blue_x, blue_y = [], []
green_x, green_y = [], []

for i in range(len(reduced_X)):
    if y[i] == 0:
        red_x.append(reduced_X[i][0])
        red_y.append(reduced_X[i][1])
    elif y[i] == 1:
        blue_x.append(reduced_X[i][0])
        blue_y.append(reduced_X[i][1])
    else:
        green_x.append(reduced_X[i][0])
        green_y.append(reduced_X[i][1])

# 数据可视化
plt.scatter(red_x, red_y, c='r', marker='x')
plt.scatter(blue_x, blue_y, c='b', marker='D')
plt.scatter(green_x, green_y, c='g', marker='.')
print(y)
plt.show()
