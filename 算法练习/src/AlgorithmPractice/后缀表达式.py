#!/usr/bin/python 
# -*- coding:utf-8 -*-

inp = list(input())
yunsuanfu = ['+', '-', '*', '/']


def getPriority(t):
    if t == '*' or t == '/':
        return 2
    elif t == '+' or t == '-':
        return 1
    else:
        return 0


stack = []
post = []
for i in range(len(inp)):
    item = inp[i]
    if item not in yunsuanfu and item != '(' and item != ')':
        post.append(item)

    if item == '(':
        stack.append(item)

    if item in yunsuanfu:
        if len(stack) == 0:
            stack.append(item)
        else:
            if getPriority(item) > getPriority(stack[-1]):
                stack.append(item)
            else:
                while len(stack) > 0 and getPriority(stack[-1]) >= getPriority(item):
                    if stack[-1] == "(":
                        stack.pop()
                        continue
                    post.append(stack.pop())
                stack.append(item)

    if item == ')':
        if stack[-1] == '(':
            stack.pop()
        else:
            while stack[-1] != '(':
                post.append(stack.pop())
            stack.pop()

if len(stack) > 0:
    for i in range(len(stack)):
        post.append(stack.pop())

for i in range(len(post)):
    if i != len(post) - 1:
        print("{}".format(post[i]), end=' ')
    else:
        print("{}".format(post[i]), end='')

