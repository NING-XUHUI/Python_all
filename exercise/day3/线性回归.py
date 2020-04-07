#!/usr/bin/python 
# -*- coding:utf-8 -*-


"""
正规方程与梯度下降
回归：
    迭代算法
    知道有误差，不断去减少误差
寻找一种能预测的趋势
线性关系：二维：直线关系
         三维：特征，目标值，平面当中
线性关系定义：
    y = kx + b  b:偏置 为了使对于单个特征的情况更加通用

多个特征：
    f(x) = w1x1 + w2x2 + w3x3 + ··· + wdxd + b
    w为权重，b称为偏置项，可以理解为w0x1

矩阵：大多数算法的计算基础

      数组：             矩阵：
0维：   5                必须是二维的
1维：[5,2,3,4,5]         满足特定运算需求：矩阵乘法（m,l）* (l,n) = (m,n)
2维：[[5,2,3,4,5]]
3维：[[[5,2,4,3,4]]]

"""

from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression, SGDRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error


def my_linear():
    """
    线性回归预测房子价格
    :return: None
    """
    # 获取数据
    lb = load_boston()
    # 分割数据集
    x_train, x_test, y_train, y_test = train_test_split(lb.data, lb.target, test_size=0.25)

    print(y_train)

    # 进行标准化
    # 特征值和目标值都进行标准化，需要两个标准化API
    std_x = StandardScaler()
    x_train = std_x.fit_transform(x_train)
    x_test = std_x.transform(x_test)

    # 目标值
    std_y = StandardScaler()
    y_train = std_y.fit_transform(y_train.reshape(-1, 1))
    y_test = std_y.transform(y_test.reshape(-1, 1))

    # estimator预测

    # 正规方程求解
    lr = LinearRegression()

    lr.fit(x_train, y_train)
    print(lr.coef_)

    # 预测测试集
    y_predict = std_y.inverse_transform(lr.predict(x_test))

    print(y_predict)
    print(mean_squared_error(std_y.inverse_transform(y_test), y_predict))
    # 梯度下降预测
    sgd = SGDRegressor()

    sgd.fit(x_train, y_train)
    print(sgd.coef_)

    # 预测测试集
    y_predict = std_y.inverse_transform(sgd.predict(x_test))

    print(y_predict)
    print(mean_squared_error(std_y.inverse_transform(y_test), y_predict))

    # 回归性能评估 均方误差

    return None


my_linear()
