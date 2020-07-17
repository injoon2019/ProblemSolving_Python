'''
Problem Solving Baekjoon 1912
Author: Injun Son
Date: July 17, 2020
'''
import copy

N = int(input())
arr = list(map(int, input().split()))

dp = copy.deepcopy(arr)

for i in range(1,N):
    dp[i] = max(dp[i], dp[i]+dp[i-1])

print(max(dp))