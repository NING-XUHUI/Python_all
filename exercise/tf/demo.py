#!/usr/bin/python 
# -*- coding:utf-8 -*-

"""
TENSORFLOW计算密集型     cpu计算

变量:todo
tensor:张量
operation:(op):专门运算的操作节点
                所有操作都是一个op
图:graph:你的整个程序的结构
会话:Session：运算程序的图

数据流图
tensor+flow
"""

"""
图:
    图moren
"""

import tensorflow as tf

# 设置警告等级
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# 实现一个加法
a = tf.constant(5.0)
b = tf.constant(6.0)

sum1 = tf.add(a, b)
print(sum1)

牛逼

with tf.Session() as sess:
    print(sess.run(sum1))

