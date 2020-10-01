#!/usr/bin/python 
# -*- coding:utf-8 -*-

number = int(input())

nums = list(map(int, input().split()))

map = {}

nums.reverse()

def DouDa(x):
    for i in range(len(map)):
        if x < map[i + 1]:
            return False
    return True


def getIndex(x):
    i = 1
    min = 0
    for j in range(len(map)):
        if x > map[j + 1]:
            continue
        else:
            if min == 0:
                min = map[j + 1] - x
                i = j + 1
            else:
                if map[j + 1] - x < min:
                    min = map[j + 1] - x
                    i = j + 1
    return i


map[1] = nums.pop()

for i in range(number - 1):
    if DouDa(nums[-1]):
        map[len(map) + 1] = nums.pop()
    else:
        if len(map) == 1:
            map[1] = nums.pop()
        else:
            map[getIndex(nums[-1])] = nums[-1]
            nums.pop()

print(len(map))
