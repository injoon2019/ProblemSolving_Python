'''
Problem Solving Baekjoon 2493
Author: Injun Son
Date: January 18, 2021
'''
import sys
from collections import deque

import heapq

N = int(input())
towers = list(map(int, input().split()))

answer = [0] * len(towers)
stack = []
for i in range(len(towers)-1, -1, -1):
    while stack and towers[i] > towers[stack[-1]]:
        answer[stack.pop()] = i+1
    stack.append(i)

print(' '.join(map(str, answer)))

