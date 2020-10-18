#!/usr/bin/python 
# -*- coding:utf-8 -*-

inp = list(input())

inp.sort()
res = {}
for i in inp:
    if i not in res:
        res[i] = 1
    else:
        res[i] += 1

for j in res:
    print("{}:{}".format(j, res[j]))
