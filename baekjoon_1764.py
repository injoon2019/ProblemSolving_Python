'''
Problem Solving Baekjoon 1764
Author: Injun Son
Date: August 24, 2020
'''
import sys
from collections import deque
from itertools import combinations
sys.setrecursionlimit(100000)

N, M = map(int, input().split())
no_heard = [input() for _ in range(N)]
no_seen = [input() for _ in range(M)]
ans = set(no_heard).intersection(set(no_seen))
ans_list = sorted(list(ans))
print(len(ans_list))
for i in ans_list:
    print(i)