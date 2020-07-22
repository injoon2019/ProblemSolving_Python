'''
Problem Solving Baekjoon 9012
Author: Injun Son
Date: July 22, 2020
'''
import sys
N = int(input())
for _ in range(N):
    stack = []
    str = input()
    is_stack = True
    for i in str:
        if i=='(':
            stack.append(i)
        elif i==")":
            if len(stack)==0:
                is_stack = False
                break
            else:
                stack.pop()

    if is_stack ==True and len(stack)==0:
        is_stack = True
    else:
        is_stack = False

    if is_stack:
        print("YES")
    else:
        print("NO")