'''
Problem Solving Baekjoon 2798
Author: Injun Son
Date: August 24, 2020
'''
import sys
from collections import deque
from itertools import combinations
sys.setrecursionlimit(100000)

N, M = map(int, input().split())
arr = list(map(int, input().split()))
comb_list = list(combinations(arr, 3))
card_sum = 0
for comb in comb_list:
    if abs(sum(comb)-M) < abs(card_sum-M) and sum(comb)<=M:
        card_sum = sum(comb)

print(card_sum)
