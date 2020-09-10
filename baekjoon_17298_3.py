'''
Problem Solving Baekjoon 17298
Author: Injun Son
Date: September 10, 2020
'''
import sys
from collections import deque

import heapq

N = int(input())
arr = list(map(int, input().split()))

stack = []
ans = [-1]*N
for i in range(len(arr)):
    while stack and arr[stack[-1]] < arr[i]:
        ans[stack.pop()] = arr[i]
    stack.append(i)

print(' '.join(list(map(str, ans))))