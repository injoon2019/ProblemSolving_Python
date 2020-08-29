'''
Problem Solving Baekjoon 10773
Author: Injun Son
Date: August 29, 2020
'''
import sys

stack = []
K = int(input())
for _ in range(K):
    a = int(input())
    if a == 0:
        stack.pop()
    else:
        stack.append(a)

print(sum(stack))