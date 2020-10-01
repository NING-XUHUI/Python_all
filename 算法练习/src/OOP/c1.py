#!/usr/bin/python 
# -*- coding:utf-8 -*-


class Student():
    # 属性，特征
    # 初始化对象的属性

    def __init__(self, name: str, age: int):
        # 构造函数
        self.name = name
        self.age = age
        print("student")

    # 行为(方法)
    def print_file(self):
        print("name: " + self.name)
        print("age: " + str(self.age))
