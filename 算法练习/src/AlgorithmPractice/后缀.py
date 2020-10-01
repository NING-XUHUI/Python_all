#!/usr/bin/python 
# -*- coding:utf-8 -*-

inp = list(input())
relin = []
others = ['+', '-', '*', '/', '(', ')']
print(inp)
for i in range(len(inp)):
    if len(relin) == 0:
        relin.append(inp[i])
    else:
        if inp[i] not in others:
            if relin[-1] == '+' and ((len(relin) == 1) or (relin[-2] == '(')):
                relin.pop()
                relin.append(inp[i])
                continue
            elif relin[-1] == '-' and ((len(relin) == 1) or (relin[-2] == '(')):
                relin[-1] += inp[i]
                continue
            elif relin[-1] not in others:
                relin[-1] += inp[i]
            else:
                relin.append(inp[i])
        else:
            relin.append(inp[i])

print(relin)

yunsuanfu = ['+', '-', '*', '/']
stack = []
post = []


def getP(t):
    if t == '*' or t == '/':
        return 2
    elif t == '+' or t == '-':
        return 1
    else:
        return 0


for i in range(len(relin)):
    item = relin[i]
    if item in yunsuanfu:
        if len(stack) == 0:
            stack.append(item)
        elif getP(item) > getP(stack[-1]):
            stack.append(item)
        else:
            while len(stack) > 0 and getP(stack[-1]) >= getP(item):
                post.append(stack.pop())
            stack.append(item)
    elif item == '(':
        stack.append(item)
    elif item == ')':
        while stack[-1] != '(':
            post.append(stack.pop())
        stack.pop()
    else:
        post.append(item)

if len(stack) > 0:
    for i in range(len(stack)):
        post.append(stack.pop())

for i in range(len(post)):
    if i != len(post) - 1:
        print("{}".format(post[i]), end=' ')
    else:
        print("{}".format(post[i]), end='')
