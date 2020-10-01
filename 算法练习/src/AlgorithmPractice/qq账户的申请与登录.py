#!/usr/bin/python 
# -*- coding:utf-8 -*-


accs = {}


def processing(ins, acc, paw):
    if ins == 'N':
        if int(acc) in accs:
            print("ERROR: Exist")
        else:
            print("New: OK")
            accs[int(acc)] = paw

    if ins == 'L':
        if int(acc) in accs:
            if accs[int(acc)] == paw:
                print("Login: OK")
            else:
                print("ERROR: Wrong PW")
        else:
            print("ERROR: Not Exist")


count = int(input())

for i in range(count):
    inputData = input().split(" ")
    instruction, account, password = list(inputData)
    processing(instruction, account, password)
