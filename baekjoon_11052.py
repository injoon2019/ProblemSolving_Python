'''
Problem Solving Baekjoon 11052
Author: Injun Son
Date: July 20, 2020
'''
import copy

N = int(input())
arr = list(map(int, input().split()))
arr = [0]+arr
dp = copy.deepcopy(arr)

dp[1] = arr[1]
for i in range(2, N+1):
    for j in range(1,i):
        dp[i] = max(dp[i], dp[i-j]+dp[j])

print(max(dp))