#!/usr/bin/python 
# -*- coding:utf-8 -*-

number = int(input())
ns = list(map(int, input().split(" ")))


def upper_bound(nums: list, target: int) -> int:
    first, last = 0, len(nums)
    while first < last:
        mid = first + (last - first) // 2
        if nums[mid] <= target:
            first = mid + 1
        else:
            last = mid
    return first


res = set([])
ns.reverse()

res.add(ns.pop())
for i in range(number - 1):
    if ns[-1] < list(res)[-1]:
        ind = upper_bound(list(res), ns[-1])
        remvNum = list(res)[ind]
        res.remove(remvNum)

    res.add(ns.pop())

print(len(res))
