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
ans = [0]*N
def get_stack_max(stack):
    tmp_max = -1
    pos = -1
    for i in range(len(stack)):
        height= stack[i][0]
        tmp_max = max(tmp_max, height)
        pos = i
    return tmp_max, pos

for i in range(len(towers)):
    if len(stack)==0:
        stack.append([towers[i], i])
        stack_max = towers[i]
        # print(i, stack)
        # print(ans)
        # print()
        continue

    if towers[i] > stack[-1][0]:
        while stack[-1][0]< get_stack_max(stack)[0]:
            _, pre_pos = stack.pop()
            towers[pre_pos] = 0
        stack.append([towers[i], i])

    elif towers[i] < stack[-1][0]:
        ans[i] = stack[-1][1]+1
        stack.append([towers[i], i])

    # print(i, stack)
    # print(ans)
    # print()

#맨마지막꺼를 빼주는 작업
stack.pop()

if len(stack)>0:
    while stack:
        h, pre_pos = stack.pop()
        if h < get_stack_max(stack)[0]:
            ans[pre_pos] = get_stack_max(stack)[1]+1

for i in ans:
    print(i, end=" ")