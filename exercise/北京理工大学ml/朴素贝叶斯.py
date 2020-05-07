#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/6 11:20 上午
# @Author  : Leoning
# @File    : 朴素贝叶斯.py

"""
朴素贝叶斯分类器是一个以贝叶斯定理为基础的多酚类的分类器
对于给定数据，首先基于特征的条件独立性假设，学习输入输出
的联合概率分布，然后基于此模型，对给定的输入x，利用贝叶斯
定理求出后验概率最大的输出y。
"""

import numpy as np
from sklearn.naive_bayes import GaussianNB

X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
Y = np.array([1, 1, 1, 2, 2, 2])

clf = GaussianNB(priors=None)
clf.fit(X, Y)
print(clf.predict([[-0.8, -1]]))
