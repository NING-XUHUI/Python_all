#!/usr/bin/python 
# -*- coding:utf-8 -*-

import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler



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
    data = pd.read_csv("datingTestSet2.txt",sep="\t")

    # 2 实例化转换器类
    # 3 调用fit_trans_form

# minmax_demo() 归一化

# stand_demo() 标准化
variance_demo()