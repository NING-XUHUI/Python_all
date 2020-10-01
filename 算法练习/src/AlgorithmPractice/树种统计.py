#!/usr/bin/python 
# -*- coding:utf-8 -*-


count = int(input())

trees = {}
all = []
for i in range(count):
    name = input()
    if hash(name) in trees:
        trees[hash(name)] += 1
    else:
        trees[hash(name)] = 1
        all.append(name)

all.sort()
for j in range(len(all)):
    print("{} {:.4f}%".format(all[j], trees[hash(all[j])] * 100/count))



