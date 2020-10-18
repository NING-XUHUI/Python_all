#!/usr/bin/python 
# -*- coding:utf-8 -*-

inp1 = input()
inp2 = list(input())
print(inp2)
print(inp1)
for i in inp2:
    if i in inp1:
        inp1 = inp1.replace(i, '')

print(inp1)
