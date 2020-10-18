#!/usr/bin/python 
# -*- coding:utf-8 -*-

count = int(input())
inp = list(map(int,input().split(" ")))

inp.sort()

Introverted = count // 2
Outgoing = count - Introverted

Diff = 0
while Outgoing!=0:
    Diff += inp[count-1] - inp[]
