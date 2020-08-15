'''
Problem Solving Baekjoon 10819
Author: Injun Son
Date: August 14, 2020
'''
import sys
import copy
from itertools import permutations
sys.setrecursionlimit(10000)

N = int(input())
arr = list(map(int, input().split()))
permute = list(permutations(arr, N))
answer = 0
for list in permute:
    sum = 0
    for i in range(0, len(list)-1):
        sum += abs(list[i] - list[i+1])

    answer = max(answer, sum)
print(answer)