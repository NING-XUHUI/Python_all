#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/6 11:11 上午
# @Author  :Leoning
# @File    : 决策树.py

"""
决策树是一树形结构的分类器，通过顺序询问分类点的属性决定分类点最终的类别。
通常根据特征的信息增益或其他指标，构造一颗决策树，在分类时，只需要按照
决策树中的结点依次进行判断，即可得到样本所属类比。
"""

from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import cross_val_score  # 交叉验证值

clf = DecisionTreeClassifier()
iris = load_iris()

"""
这里我们将决策树分类器作为待评估的模型，iris.data鸢尾花数据作为特征
，iris.target鸢尾花分类标签作为目标结果，通过设定cv为10，使用10折
交叉验证。得到最终交叉验证得分。
"""
cross_val_score(clf, iris.data, iris.target, cv=10)

"""
clf.fit(X,y)
clf.predict(x)
"""
