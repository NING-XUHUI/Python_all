#!/usr/bin/python 
# -*- coding:utf-8 -*-

from sklearn.datasets import fetch_20newsgroups
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report


"""
概率基础：
    按概率最大分类

朴素贝叶斯：
    特征独立
    文档分类
    
优点：
    1、朴素贝叶斯模型发源于古典数学理论，有稳定的分类效率
    2、对确实数据不太敏感，算法也比较简单，用用于文本分类。
    3、分类准确度高，速度快
缺点：
    由于使用了样本数学独立性的假设，所以如果样本数学有关联时其效果不好
"""


def naviebayes():
    """
    朴素贝叶斯进行文本分类
    :return:
    """
    news = fetch_20newsgroups(subset='all')
    x_train, x_test, y_train, y_test = train_test_split(news.data, news.target, test_size=0.25)

    # 对数据集进行特征抽取
    tf = TfidfVectorizer()
    # 以训练集当中的此地列表进行每篇文章重要性统计
    x_train = tf.fit_transform(x_train)
    print(tf.get_feature_names())
    x_test = tf.transform(x_test)

    # 进行朴素贝叶斯算法的预测
    mlt = MultinomialNB(alpha=1.0)
    print(x_train.toarray())
    mlt.fit(x_train, y_train)

    y_predict = mlt.predict(x_test)

    # 得出准确率

    print(mlt.score(x_test, y_test))
    print("精确率和召回率:",classification_report(y_test,y_predict,target_names=news.target_names))

    return None


naviebayes()
