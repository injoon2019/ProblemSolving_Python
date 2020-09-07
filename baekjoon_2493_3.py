'''
Problem Solving Baekjoon 2493
Author: Injun Son
Date: September 7, 2020
'''
import sys
from collections import deque

import heapq
N = int(input())
towers = list(map(int, input().split()))
arr = [0]*N
stack = []

for i in range(len(towers)):
    t = towers[i]
    while stack and towers[stack[-1]] < t:
        stack.pop()

    if stack:
        arr[i] = stack[-1]+1

    stack.append(i)

print(' '.join(list(map(str, arr))))