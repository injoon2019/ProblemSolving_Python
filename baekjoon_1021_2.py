'''
Problem Solving Baekjoon 1021_2
Author: Injun Son
Date: July 30, 2020
'''
import sys
from collections import deque
sys.setrecursionlimit(100000)

n, m = map(int, input().split())
target_list = map(int, input().split())
q_list = deque([i for i in range(1, n+1)])

result  = 0
for find_num in target_list:
    target_idx = q_list.index(find_num)

    movement_cnt = target_idx
    if target_idx > len(q_list)-target_idx:
        #movement_cnt = len(q_list) - target_idx
        movement_cnt -= len(q_list)

    result += abs(movement_cnt)
    q_list.rotate(-movement_cnt)
    q_list.popleft()

print(result)