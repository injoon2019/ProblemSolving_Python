'''
Problem Solving Baekjoon 17298
Author: Injun Son
Date: September 7, 2020
'''
import sys
from collections import deque

import heapq

N = int(input())
arr = list(map(int, input().split()))
stack = []
ans = [-1]*N

for i in range(N):
    ai = arr[i]
    #더 큰 수를 만나면 쭉 비워낸다
    while stack and arr[stack[-1]] <ai:
        ans[stack.pop()] = ai

    #그러고도 스택에 남아있으면 그건 스택이 더 큰거다
    stack.append(i)

print(' '.join(list(map(str, ans))))