#!/usr/bin/python 
# -*- coding:utf-8 -*-
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.feature_extraction import DictVectorizer
from sklearn.tree import DecisionTreeClassifier, export_graphviz

"""
决策树的分类依据之一：
    1 信息熵
      信息增益
    2 ID3
    3 C4.5
    4 CART
    回归树：
    分类树：基尼系数（划分更加细致）
    DecisionTree
"""


def decision():
    """
    决策树对泰坦尼克号进行生死预测
    :return:None
    """
    # 获取数据
    titan = pd.read_csv("./titanic/train.csv")
    y_test = pd.read_csv("./titanic/gender_submission.csv")
    x_test = pd.read_csv("./titanic/test.csv")
    # 处理数据

    x_test = x_test[['Pclass', 'Age', 'Sex']]
    x_train = titan[['Pclass', 'Age', 'Sex']]
    y_train = titan['Survived']

    # 缺失值处理
    x_train['Age'].fillna(x_train['Age'].mean(), inplace=True)
    x_test['Age'].fillna(x_test['Age'].mean(), inplace=True)

    print(x_train)
    # 分割数据
    # 已分割

    # 进行处理  特征工程  类别处理：one-hot编码
    dict = DictVectorizer(sparse=False)
    x_train = dict.fit_transform(x_train.to_dict(orient="records"))
    print(dict.get_feature_names())
    x_test = dict.transform(x_test.to_dict(orient="records"))

    # print(x_train)

    # 决策树进行预测
    dec = DecisionTreeClassifier()

    dec.fit(x_train, y_train)
    prediction = dec.predict(x_test)
    # print(prediction)

    # 预测准确率
    # print(x_train,y_train)
    print(dec.score(x_train, y_train))

    export_graphviz(dec, out_file="./tree.dot", feature_names=['Age', 'Pclass', 'Sex=female', 'Sex=male'])
    return None


decision()
