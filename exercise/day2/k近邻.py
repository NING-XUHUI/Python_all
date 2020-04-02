#!/usr/bin/python 
# -*- coding:utf-8 -*-
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler


"""
分类：
    特征值：x，y坐标，定位准确性，时间
    目标值：入住位置的id

处理：
    0<x<10  0<y<10
    1、由于数据量大，缩小x，y
    2、时间戳进行（年月日···），当作新的特征
    3、入住id种类过多，将少于指定人数的位置删除
    
一、k值该取多大？有什么影响？
    k值取得很小：容易受异常点影响
    k值取得很大：容易受k值数量（类别）波动
二、性能问题？
    时间复杂度高
"""


def knncls():
    """
    用户入住位置
    :return:
    """
    # 读取数据

    data = pd.read_csv("./train.csv")

    # 处理数据
    # 缩小数据范围,查询数据筛选
    data = data.query("x > 1.0 & x < 1.25 & y > 2.5 & y < 2.75")

    # 处理时间数据
    time_value = pd.to_datetime(data["time"], unit='s')
    # print(time_value)
    # 把日期格式转为字典
    time_value = pd.DatetimeIndex(time_value)

    # 构造特征
    data['day'] = time_value.day
    data['hour'] = time_value.hour
    data['weekday'] = time_value.weekday

    # 删除时间戳
    data.drop(['time'], axis=1)

    # 把签到数量少于N个目标位置删除
    place_count = data.groupby('place_id').count()
    tf = place_count[place_count.row_id > 3].reset_index()

    data = data[data['place_id'].isin(tf.place_id)]
    data.drop('row_id', axis=1)
    # 去除特征值和目标值
    y = data['place_id']
    x = data.drop(['place_id'], axis=1)

    # 数据分割
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25)

    # 特征工程（标准化）十分重要
    std = StandardScaler()
    # 对测试集和训练集对特征值进行标准化
    x_train = std.fit_transform(x_train)

    x_test = std.transform(x_test)

    # 进行算法流程
    knn = KNeighborsClassifier(n_neighbors=5)

    # fit
    knn.fit(x_train, y_train)
    # 得出预测
    y_predict = knn.predict(x_test)

    # 预测准确率
    print(knn.score(x_test, y_test))

    return None


knncls()
