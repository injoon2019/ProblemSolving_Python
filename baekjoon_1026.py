'''
Problem Solving Baekjoon 1026
Author: Injun Son
Date: October 15, 2020
'''
import sys
from collections import deque
sys.setrecursionlimit(100000)

N = int(input())
arr_a = list(map(int, input().split()))
arr_b = list(map(int, input().split()))

arr_a.sort()
arr_b.sort(reverse=True)

ans = 0
for i in range(N):
    ans += arr_a[i]*arr_b[i]

print(ans)