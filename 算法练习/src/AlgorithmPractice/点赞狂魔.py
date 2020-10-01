#!/usr/bin/python 
# -*- coding:utf-8 -*-

count = int(input())

data = {}
# data1 = {}
# data2 = {}

for i in range(count):
    inp = list(input().split(" "))
    name = inp[0]
    dianzan = list(map(int, inp[2:]))
    a = len(set(dianzan))
    b = len(dianzan) / a
    data[name] = [a, b]

# print(data)
a = sorted(data.items(), key=lambda x: (-x[1][0], x[1][1]))
if len(a) >= 3:
    a = a[:3]
    print("{} {} {}".format(a[0][0], a[1][0], a[2][0]))
else:
    a = a[:len(a)]
    for i in range(len(a)):
        print("{} ".format(a[i][0]), end='')
    for j in range(3 - len(a)):
        if j == 3 - len(a) - 1:
            print("-", end='')
        else:
            print("-", end=' ')
