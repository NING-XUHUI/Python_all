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
    1、图默认已经注册，一组表示tf.Operation计算单位的对象和tf.Tensor表示
操作之间流动的数据单元对象
    2、获取调用：
        - tf.get_default_graph()
        - op、sess或者tensor的graph属性
    
"""

"""
会话：
    1、运行图的结构
    2、分配资源计算
    3、掌握资源（变量的资源，队列，线程）
会话run：
    运算ops和计算tensor
    
"""

import tensorflow as tf

# 设置警告等级
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# 创建一张图包含了一组op和tensor,上下文环境
# op：只要使用tensorflow的API定义的函数都是OP
# tensor:指代的是数据

# 重载机制,默认给运算符重载为op类型


# g = tf.Graph()
#
# print(g)
# with g.as_default():
#     c = tf.constant(11.0)
# print(c.graph)
#
# # 实现一个加法
# a = tf.constant(5.0)
# b = tf.constant(6.0)
#
# sum1 = tf.add(a, b)
# print(sum1)
#
# # 默认的这张图，相当于市程序分配的一段内存
# graph = tf.get_default_graph()
# print(graph)
#
# # 只能运行一个图
# # 只要有上下文环境，就可以使用方便的eval
#
# # 训练模型
# # 实时提供数据进行训练
# # placeholder是一个占位符,feed_dict是一个字典
# plt = tf.placeholder(tf.float32, shape=[None, 3])# 行数不确定
#
# with tf.Session() as sess:
#     print(sess.run(plt, feed_dict={plt: [[1, 2, 3], [4, 5, 6]]}))
#     print(a.graph)
#     print(sum1.graph)
#     print(sess.graph)

# 形状的概念
# 静态形状和动态形状
# 对于静态形状来说，一旦张量形状固定了，就不能再次设置静态形状
# 动态形状可以去创建一个新的张量,动态形状改变时，要注意元素数量要匹配

plt = tf.placeholder(tf.float32, [None, 2])
print(plt)
plt.set_shape([3, 2])
print(plt)

plt_reshape = tf.reshape(plt, [2, 3, 1])
print(plt_reshape)

with tf.Session as sess:
    pass
