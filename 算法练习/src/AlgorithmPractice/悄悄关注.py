#!/usr/bin/python 
# -*- coding:utf-8 -*-

inputData = input().split(" ")

names = list(inputData)
count = int(names[0])
del names[0]

curhash = {}
for k in range(count):
    curhash[hash(names[k])] = names

hash_s = {}
hash_d = {}
sum = 0
num = int(input())
for i in range(num):
    inp = input().split(" ")
    name, dianzan = list(inp)
    hash_d[hash(name)] = int(dianzan)
    hash_s[hash(name)] = name
    sum += int(dianzan)

avg = sum / num

outp = []
for hv in hash_d:
    if hash_d[hv] > avg and hv not in curhash:
        outp.append(hash_s[hv])

outp.sort()
if len(outp) == 0:
    print("Bing Mei You")
else:
    for i in range(len(outp)):
        print("{}".format(outp[i]))



