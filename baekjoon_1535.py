'''
Problem Solving Baekjoon 1535
Author: Injun Son
Date: August 25, 2020
'''
import sys
from collections import deque
from itertools import combinations
from itertools import permutations
import math
sys.setrecursionlimit(100000)

N= int(input())
hp_loss = list(map(int, input().split()))
happiness = list(map(int, input().split()))

friends = [False]*N
max_happiness = -1*sys.maxsize
def back_tracking(cur_num, cur_hp, cur_hap, max_num):
    global max_happiness
    if cur_num >=max_num:
        return

    if cur_hp - hp_loss[cur_num] > 0:
        max_happiness = max(max_happiness, cur_hap+happiness[cur_num])
        back_tracking(cur_num+1, cur_hp - hp_loss[cur_num], cur_hap+happiness[cur_num], max_num)
    else:
        max_happiness = max(max_happiness, cur_hap)
        back_tracking(cur_num+1, cur_hp, cur_hap, max_num)

back_tracking(0, 100, 0, N)
print(max_happiness)