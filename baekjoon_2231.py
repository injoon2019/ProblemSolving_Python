'''
Problem Solving Baekjoon 2231
Author: Injun Son
Date: August 24, 2020
'''
import sys
from collections import deque
from itertools import combinations
sys.setrecursionlimit(100000)

N = int(input())
arr = list(map(int, str(N)))

for i in range(1, N):
    arr = list(map(int, str(i)))
    sum_num = sum(arr)+i
    if sum_num == N:
        print(i)
        exit()

print(0)