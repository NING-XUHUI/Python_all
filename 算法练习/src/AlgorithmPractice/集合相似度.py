#!/usr/bin/python 
# -*- coding:utf-8 -*-
import datetime
def compute(set1, set2):
    a1 = set(set1 + set2)
    ss1 = set(set1)
    ss2 = set(set2)
    iset = ss1 & ss2
    print("{:.2f}%".format(len(iset) * 100 / len(a1)))


setsCount = int(input())

sets = {}
for i in range(setsCount):
    data = input().split(" ")
    tset = list(map(int, data))
    del tset[0]
    sets[(i + 1)] = tset

count = int(input())

for j in range(count):
    a = input().split(" ")
    s1, s2 = list(map(int, a))
    start = datetime.datetime.now()
    compute(sets[s1], sets[s2])
    end = datetime.datetime.now()
    print(end-start)
