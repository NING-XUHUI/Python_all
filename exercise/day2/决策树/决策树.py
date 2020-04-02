#!/usr/bin/python 
# -*- coding:utf-8 -*-
import pandas as pd
from sklearn.model_selection import train_test_split
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
    
决策树的优缺点：
    优点：1-简单的理解和解释，树木可视化
         2-需要很少的数据准备，其他技术通常需要数据归一化
    缺点：1-决策树学习者可以创建不能很好地推广数据的过于复杂的树，这被称为过拟合。
    改进：1-减枝cart算法（决策树API当中已经实现，随机森林参数调优有关介绍）
         2-随机树林
    注意：企业重要决策，由于决策树很好的分析能力，在决策过程应用较多
"""


def decision():
    """
    决策树对泰坦尼克号进行生死预测
    :return:None
    """
    # 获取数据
    titan = pd.read_csv("./titanic/train.csv")
    pre = pd.read_csv("./titanic/test.csv")
    # 处理数据
    x = titan[['Pclass', 'Age', 'Sex']]
    pre = pre[['Pclass', 'Age', 'Sex']]
    y = titan['Survived']

    # 缺失值处理
    x['Age'].fillna(x['Age'].mean(), inplace=True)
    pre['Age'].fillna(pre['Age'].mean(),inplace=True)

    # 分割数据

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25)


    # 进行处理  特征工程  类别处理：one-hot编码
    dict = DictVectorizer(sparse=False)
    x_train = dict.fit_transform(x_train.to_dict(orient="records"))
    pre = dict.transform(pre.to_dict(orient="records"))
    print(dict.get_feature_names())
    x_test = dict.transform(x_test.to_dict(orient="records"))

    # print(x_train)

    # 决策树进行预测
    dec = DecisionTreeClassifier()

    dec.fit(x_train, y_train)

    # print(prediction)

    # 预测准确率

    prediction = dec.predict(pre)
    print(dec.score(x_test, y_test))
    print(prediction)

    # export_graphviz(dec, out_file="./tree.dot", feature_names=['Age', 'Pclass', 'Sex=female', 'Sex=male'])
    return None


decision()
