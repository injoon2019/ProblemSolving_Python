'''
Problem Solving Baekjoon 13398
Author: Injun Son
Date: September 16, 2020
'''
from collections import deque
import heapq
import sys, copy

input= sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
dp = [ [0,0] for _ in range(n)]
#dp[i][0]는 제외하지 않았을 때 최대연속합
#dp[i][1]은 제외했을 때 최대연속합

dp[0][0] = arr[0]
ans = arr[0]
for i in range(1, n):
    dp[i][0] = max(arr[i], dp[i-1][0]+arr[i])
    dp[i][1] = max(arr[i], dp[i-1][1]+arr[i], dp[i-1][0])
    ans = max(ans, dp[i][0], dp[i][1])
print(ans)