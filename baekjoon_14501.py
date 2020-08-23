'''
Problem Solving Baekjoon 14501
Author: Injun Son
Date: August 23, 2020
'''
from collections import deque
import sys
N = int(input())
time_arr, pay_arr = [], []

dp = [0]*N
#dp[i] = i일째까지 i를 선택했을때 max 값
for _ in range(N):
    time, pay = map(int, input().split())
    time_arr.append(time)
    pay_arr.append(pay)

for i in range(0, N):
    if i+time_arr[i]-1<N:
        dp[i]=pay_arr[i]
        max_tmp = 0
        for j in range(0, i):
            if j+ time_arr[j]-1 < i:
                max_tmp = max(max_tmp, dp[j])
        dp[i] += max_tmp

print(max(dp))