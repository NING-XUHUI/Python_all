#!/usr/bin/python 
# -*- coding:utf-8 -*-

"""
tf.Variable
变量也是一种op，是一种特殊的张量，能够进行存储持久化，他的值就是
张量，默认被训练
"""

import tensorflow as tf

x = tf.Variable([1, 2])
a = tf.constant([3, 3])

# 变量需要初始化
init = tf.global_variables_initializer()

# 加减法op
sub = tf.subtract(x, a)
add = tf.add(x, a)

with tf.Session() as sess:
    sess.run(init)
    print(sess.run(sub))
    print(sess.run(add))

# 创建一个变量初始化为0
state = tf.Variable(0, name='counter')
# 创建op，作用是使state加1
new_value = tf.add(state, 1)
# 赋值op
update = tf.assign(state, new_value)
init = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)
    print(sess.run(state))
    for _ in range(5):
        sess.run(update)
        print(sess.run(state))

