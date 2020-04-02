#!/usr/bin/python 
# -*- coding:utf-8 -*-

from sklearn.datasets import load_iris, fetch_20newsgroups, load_boston
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction import DictVectorizer


def iris():
    """
    莺尾花
    :return:
    """

    data = load_iris()

    x_train, x_test, y_train, y_test = train_test_split(data.data, data.target, test_size=0.25)

    mlt = MultinomialNB(alpha=1.0)  # 拉普拉斯平滑值

    mlt.fit(x_train, y_train)

    y_predict = mlt.predict(x_test)

    print(mlt.score(x_test, y_test))


iris()
