#!/usr/bin/python 
# -*- coding:utf-8 -*-

inp = input()
a, n = map(int,inp.split(" "))
sum = 0
for i in range(n):
    sum += a
    a = a + a * 10

print(sum)

