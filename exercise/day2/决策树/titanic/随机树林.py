#!/usr/bin/python 
# -*- coding:utf-8 -*-
import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.feature_extraction import DictVectorizer
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn.ensemble import RandomForestClassifier

"""
    随机树林建立多个决策树过程：
        单个树建立过程：
            1、随机在N个样本中选择一个样本，重复N次，样本有可能重复
            2、随机在M个特征当中选出m个特征
        多个决策树建立：
            样本特征大多不一样   随机又放回的抽样bootstrap
            
    为什么要随机抽
样训练集？
        如果不进行随机抽样，每棵树的训练集都一样，那么最终训练出的树分类结果也是完全一样的
    为什么要有放回的抽样？
        如果不是有放回的抽样，那么每棵树的训练样本都是不同的，都是没有交集的，这样每棵树都是"有偏的"，都是绝对"片面的"，也就是说
        没课树训练出来都是有很大的差异：而随机森林最后分类取决于多棵树（弱分类器）的投票表决。
        
    随机森林参数：
        1、n_estimator 
        2、max_depth
        
    随机森林的优点：
        1、在当前所有算法中，具有极好的准确率
        2、能够有效的运行在大数据集上
        3、能够处理具有高维特征的输入样本，而且不需要降维
        4、能够评估各个特征在分类问题上的重要性
"""


def decision():
    """
    决策树对泰坦尼克号进行生死预测
    :return:None
    """
    # 获取数据
    titan = pd.read_csv("./train.csv")
    pre = pd.read_csv("./test.csv")
    # 处理数据
    x = titan[['Pclass', 'Age', 'Sex']]
    pre = pre[['Pclass', 'Age', 'Sex']]
    y = titan['Survived']

    # 缺失值处理
    x['Age'].fillna(x['Age'].mean(), inplace=True)
    pre['Age'].fillna(pre['Age'].mean(), inplace=True)

    std = StandardScaler()

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
    # dec = DecisionTreeClassifier()
    #
    # dec.fit(x_train, y_train)
    #
    # # print(prediction)
    #
    # # 预测准确率
    #
    # prediction = dec.predict(pre)
    # print(dec.score(x_test, y_test))
    # print(prediction)

    # 随机森林进行预测（超参数调优）

    rf = RandomForestClassifier()

    param = {"n_estimators": [50, 100, 200, 300, 500, 800, 1200], "max_depth": [5, 8, 15, 25, 30]}
    # 网格搜索与交叉验证

    gc = GridSearchCV(rf, param_grid=param, cv=2)

    gc.fit(x_train, y_train)

    print("准确率", gc.score(x_test, y_test))

    predicton = gc.predict(pre)
    print("最好结果：", gc.best_params_)

    print(predicton)
    export_graphviz(decision_tree=5, out_file="./randomtree.dot",
                    feature_names=['Age', 'Pclass', 'Sex=female', 'Sex=male'])
    return None


decision()
