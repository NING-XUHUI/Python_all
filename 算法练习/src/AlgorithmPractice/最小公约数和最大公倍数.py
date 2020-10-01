#!/usr/bin/python 
# -*- coding:utf-8 -*-

a, b = list(map(int, input().split(" ")))

if a == b:
    print("{}".format(a))
    print("{}".format(a))
else:
    if a < b:
        a, b = b, a
        g = a
        l = b

    g = a
    l = b
    c = a % b
    while c != 0:
        a = b
        b = c
        c = a % b

    print("{}".format(b))
    print("{}".format(int(g * l / b)))

