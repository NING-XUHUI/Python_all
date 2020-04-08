#!/usr/bin/python 
# -*- coding:utf-8 -*-

"""
逻辑回归（二分类问题）：
    线性回归的式子作为输入
    也能得出概率值

广告点击（有没有点击？）：

线性回归的输入----->分类
sigmoid函数：
    [0，1]之间的值～概率

逻辑回归的损失函数：
    对数似然损失函数

逻辑回归总结：
    应用：
        广告点击率预测、是否患病、金融诈骗、是否为虚假账号
    优点：
        适合需要得到一个分类概率的场景，简单，速度快
    缺点：
        不好处理多分类问题

朴素贝叶斯适合文本分类的多分类问题
"""
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report


def logistic():
    """
    逻辑回归做二分类进行癌症预测
    :return: None
    """
    # 构造列标签
    column = ['Sample code number', 'Clump Thickness', 'Uniformity of Cell Size', 'Uniformity of Cell Shape',
              'Marginal Adhesion', 'Single Epithelial Cell Size', 'Bare Buclei', 'Bland Chromatin', 'Normal Nucleoli',
              'Mitoses', 'Class']

    # 读取数据
    data = pd.read_csv("./Breast-Cancer/breast-cancer-wisconsin.data.txt", names=column)
    # print(data.head(10))

    # 缺失值处理
    data = data.replace(to_replace='?', value=np.nan)
    data = data.dropna()

    # 进行数据分割
    x_train, x_test, y_train, y_test = train_test_split(data[column[1:10]], data[column[10]], test_size=0.25)

    # 进行标准化处理
    std = StandardScaler()
    x_train = std.fit_transform(x_train)
    x_test = std.transform(x_test)

    # 逻辑回归
    lg = LogisticRegression(C=1.0)
    lg.fit(x_train, y_train)
    y_pre = lg.predict(x_test)
    print(lg.coef_)
    print(lg.score(x_test, y_test))
    print(classification_report(y_test, y_pre, labels=[2, 4], target_names=["良性", "恶性"]))

    return None


logistic()
