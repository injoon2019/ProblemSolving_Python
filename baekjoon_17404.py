'''
Problem Solving Baekjoon 17404
Author: Injun Son
Date: September 25, 2020
'''
from collections import deque
import sys
from itertools import combinations
#https://cooling.tistory.com/4
n = int(input())
cost = []

for _ in range(n):
    cost.append(list(map(int, input().split())))

ans = sys.maxsize
for initcolor in range(3):
    #dp[색][집]
    dp = [[0 for _ in range(n)] for _ in range(3)]

    for i in range(3):
        if i==initcolor:
            dp[i][0] = cost[0][i]
            continue
        dp[i][0] = 987654321

    for i in range(1, n):
        dp[0][i] = cost[i][0] + min(dp[1][i-1], dp[2][i-1])
        dp[1][i] = cost[i][1] + min(dp[0][i-1], dp[2][i-1])
        dp[2][i] = cost[i][2] + min(dp[0][i-1], dp[1][i-1])

    for i in range(3):
        if i==initcolor:
            continue
        ans = min(ans, dp[i][-1])

print(ans)