#!/usr/bin/python 
# -*- coding:utf-8 -*-
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
import jieba
from sklearn.preprocessing import MinMaxScaler
from sklearn.impute import SimpleImputer


def countvec():
    """
    对文本进行特征值化
    :return:
    """
    cv = CountVectorizer()

    data = cv.fit_transform(["今天很残酷，明天更残酷，后天很美好，但绝对大部分是死在明天晚上，所以每个人不要放弃今天",
                             "我们看到的从很远星系来的光是几百万年前发出的，这样当我们看到宇宙时，我们是在看他的过去",
                             "如果只用一种方式了解某一事物，你就不会真正了解他。了解事物真正含义但秘密取决于如何将其与我们所了解但事物相关联。"])

    # 单个字母不统计 没有分类依据

    print(cv.get_feature_names())
    print(data.toarray())

    return None


def cutword():
    con1 = jieba.cut("今天很残酷，明天更残酷，后天很美好，但绝对大部分是死在明天晚上，所以每个人不要放弃今天")
    con2 = jieba.cut("我们看到的从很远星系来的光是几百万年前发出的，这样当我们看到宇宙时，我们是在看他的过去")
    con3 = jieba.cut("如果只用一种方式了解某一事物，你就不会真正了解他。了解事物真正含义但秘密取决于如何将其与我们所了解但事物相关联。")

    # 转换成列表

    content1 = list(con1)
    content2 = list(con2)
    content3 = list(con3)

    # 把列表转换成字符串

    c1 = ' '.join(content1)
    c2 = ' '.join(content2)
    c3 = ' '.join(content3)

    return c1, c2, c3


def hanzivec():
    """
    中文特征值化
    :return:
    """
    c1, c2, c3 = cutword()

    cv = CountVectorizer()

    data = cv.fit_transform([c1, c2, c3])

    # 单个字母不统计 没有分类依据

    print(cv.get_feature_names())
    print(data.toarray())

    return None


def tfidvec():
    """
    中文特征值化
    :return:
    """
    c1, c2, c3 = cutword()

    tf = TfidfVectorizer()

    data = tf.fit_transform([c1, c2, c3])

    # 单个字母不统计 没有分类依据

    print(tf.get_feature_names())
    print(data.toarray())

    return None


def mm():
    """
    归一化处理
    :return:
    """

    mm = MinMaxScaler(feature_range=(2, 3))

    data = mm.fit_transform([[90, 2, 10, 40], [60, 4, 15, 45], [75, 3, 13, 46]])

    print(data)

    return None


tfidvec()
