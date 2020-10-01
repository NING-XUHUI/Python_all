#!/usr/bin/python 
# -*- coding:utf-8 -*-

a = input().split(" ")
stuCount, courseCount = list(map(int, a))
s_c = {}
for i in range(courseCount):
    a = input().split(" ")
    cname, scount = list(map(int, a))
    if scount <= 0:
        continue

    name = list(input().split(" "))
    for j in range(len(name)):
        vhash = hash(name[j])
        if vhash in s_c:
            s_c[vhash].append(cname)
        else:
            s_c[vhash] = []
            s_c[vhash].append(cname)

name = list(input().split(" "))
for j in range(len(name)):
    vhash = hash(name[j])
    print("{} {}".format(name[j], len(s_c[vhash])), end='')
    for k in range(len(s_c[vhash])):
        if k == len(s_c[vhash]) - 1:
            print(" {}".format(s_c[vhash][k]))
        else:
            print(" {}".format(s_c[vhash][k]), end='')
