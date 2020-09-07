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
stack = []
arr = [0]*N

for i in range(N):
    t = towers[i]
    # 현재 타워보다 작은 타워들은 어짜피 쓸모가 없다.
    while stack and towers[stack[-1]] <t:
        stack.pop()
    # 위 과정을 거치고도 남아있는 타워는 현재 타워보다 왼쪽에 있는 가장 가깝고 큰 타워이다.
    if stack:
        arr[i] = stack[-1] +1
    stack.append(i)

print(' '.join(list(map(str, arr))))