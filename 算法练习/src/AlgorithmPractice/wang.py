#!/usr/bin/python 
# -*- coding:utf-8 -*-

a, b = list(map(int, input().split(" ")))

sum = a + b
for i in range(sum):
    print("Wang!", end='')
