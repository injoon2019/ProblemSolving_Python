'''
Problem Solving Baekjoon 11652_4
Author: Injun Son
Date: August 24, 2020
'''
import sys
from collections import Counter

input = sys.stdin.readline
N = int(input())
check = dict()
for _ in range(N):
    a = int(input())
    if a in check:
        check[a]+=1
    else:
        check[a]=1

arr = [(key, val) for key, val in check.items()]
arr = sorted(arr, key= lambda x: (-x[1], x[0]))
print(arr[0][0])
