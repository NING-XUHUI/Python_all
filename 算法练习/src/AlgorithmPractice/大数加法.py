#!/usr/bin/python 
# -*- coding:utf-8 -*-

p1 = list(input())
p2 = list(input())
res = []
zero = [0]
flag = 0

if len(p1) == len(p2):
    times = len(p1) + 1
    p1 = zero + p1
    p2 = zero + p2
if len(p1) > len(p2):
    times = len(p1) + 1
    zeros = [0] * (times - len(p2))
    p1 = zero + p1
    p2 = zeros + p2
if len(p1) < len(p2):
    times = len(p2) + 1
    zeros = [0] * (times - len(p1))
    p2 = zero + p2
    p1 = zeros + p1


while times != 0:
    sum = int(p1.pop()) + int(p2.pop()) + flag
    if sum >= 10:
        sum = sum % 10
        flag = 1
    else:
        flag = 0
    res.append(str(sum))
    times -= 1


sum = 0
for i in range(len(res)):
    sum += int(res[i]) * (10 ** i)

print(sum)