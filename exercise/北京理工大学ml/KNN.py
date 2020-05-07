#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/6 11:04 上午
# @Author  :Leoning
# @File    : KNN.py

"""
在实际使用时，我们可以使用所有训练数据构成特征X和标签y，使用fit()函数进行训练。
在正式分类时，通过一次性构造测试集或者一个一个输入样本的方式，得到样本对应的
分类结果，有关K的取值：
1、如果较大，相当于使用较大邻域内的训练实例进行预测，可以减少估计误差，但是距离
较远的样本也会对预测起作用，导致预测错误。
2、如果较小，相当于使用较小的邻域进行预测，如果邻居恰好是噪声点，会导致过拟合。
"""

from sklearn.neighbors import KNeighborsClassifier

X = [[0], [1], [2], [3]]
y = [0, 0, 1, 1]

neigh = KNeighborsClassifier(n_neighbors=3)
neigh.fit(X, y)
print(neigh.predict([[1.1]]))
