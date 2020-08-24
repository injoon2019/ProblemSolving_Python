'''
Problem Solving Baekjoon 14888
Author: Injun Son
Date: August 24, 2020
'''
import sys
from collections import deque
from itertools import combinations
from itertools import permutations
import math
sys.setrecursionlimit(100000)

N= int(input())
arr = list(map(int, input().split()))
plus, minus, multiply, divide = map(int, input().split())
operators = []
operators+= (["+"]*plus)
operators+=(["-"]*minus)
operators+=(["*"]*multiply)
operators+=(["/"]*divide)
possible_combs = list(permutations([i for i in range(0, N-1)]))
possible_combs = set(possible_combs)
max_val = -999999
min_val = sys.maxsize

for comb in possible_combs:
    tmp_val = arr[0]
    for i in range(1, len(arr)):
        if operators[comb[i-1]]=='+':
            tmp_val += arr[i]
        elif operators[comb[i-1]]=='-':
            tmp_val -= arr[i]
        if operators[comb[i-1]]=='*':
            tmp_val *= arr[i]
        if operators[comb[i-1]]=='/':
            if tmp_val <0:
                tmp_val = (abs(tmp_val)//arr[i])*-1
            else:
                tmp_val //= arr[i]

    if tmp_val > max_val:
        max_val = tmp_val
    if tmp_val < min_val:
        min_val = tmp_val

print(max_val)
print(min_val)