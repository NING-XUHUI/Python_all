#!/usr/bin/python 
# -*- coding:utf-8 -*-

import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
from sklearn.feature_selection import VarianceThreshold
from scipy.stats import pearsonr
from sklearn.decomposition import PCA


def minmax_demo():
    """
    归一化
    缺点：只适合传统精确小数据场景
    :return:
    """
    # 1.获取数据
    data = pd.read_csv("datingTestSet2.txt", sep="\t")
    data = data.iloc[:, :3]
    # print("data:\n", data)
    # 2.实例化一个转换器类
    # transfer = MinMaxScaler()
    transfer = MinMaxScaler(feature_range=(1, 2))
    # 3.调用fit_transform
    data_new = transfer.fit_transform(data)
    print(data_new)
    return None


def stand_demo():
    """
    标准化
    适合现代嘈杂大数据场景
    :return:
    """
    # 1.获取数据
    data = pd.read_csv("datingTestSet2.txt", sep="\t")
    data = data.iloc[:, :3]
    # print("data:\n", data)
    # 2.实例化一个转换器类
    transfer = StandardScaler()
    # 3.调用fit_transform
    data_new = transfer.fit_transform(data)
    print(data_new)
    return None


def variance_demo():
    """
    低方差特征过滤
    :return:
    """
    # 1 获取数据
    data = pd.read_csv("datingTestSet2.txt", sep="\t")
    data = data.iloc[:, :3]
    # 2 实例化转换器类
    transfer = VarianceThreshold(threshold=0.0)
    data_new = transfer.fit_transform(data)
    print(data_new)
    # 3 调用fit_trans_form
    r = pearsonr(data["miles"], data["game"])
    # print("相关系数", r)


def PCA_demo():
    """
    PCA降维
    :return:
    """
    data = [[2, 8, 4, 5],
            [6, 3, 0, 8],
            [5, 4, 9, 1]]
    print(data)
    # 1 实例化一个转化器类
    transform = PCA(n_components=1)
    # 2 调用fit_transform
    data_new = transform.fit_transform(data)

    print(data_new)
    return None


def var():
    var = VarianceThreshold(threshold=1.0)
    data = var.fit_transform([[0, 2, 0, 3], [0, 1, 4, 3], [0, 1, 1, 3]])
    print(data)


# minmax_demo() 归一化
# stand_demo()
variance_demo()
# PCA_demo()
# var()