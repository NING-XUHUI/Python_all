#!/usr/bin/python 
# -*- coding:utf-8 -*-


class Student():
    # 属性，特征
    # 初始化对象的属性
    sum1 = 0

    def __init__(self, name: str, age: int):
        # 构造函数
        self.name = name
        self.age = age
        self.__score = 10
        self.plus_sum()
        print("there is(are) {0} student(s)".format(self.__class__.sum1))

    def __marking__(self, score):
        self.__score = score
        print(self.__score)

    # 行为(方法)
    @classmethod
    def plus_sum(cls):
        cls.sum1 += 1

    def print_file(self):
        print("name: " + self.name)
        print("age: " + str(self.age))

    @staticmethod
    def add(x, y):
        print(Student.sum1)


student1 = Student(name='石敢当', age=18)
student2 = Student(name='宁旭晖', age=18)
