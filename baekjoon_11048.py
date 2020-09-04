'''
Problem Solving Baekjoon 11048
Author: Injun Son
Date: September 3, 2020
'''
from collections import deque
import sys

import sys

r, c = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(r)]
dp = [[0]*c for _ in range(r)]

dp[0][0] = graph[0][0]
for i in range(r):
    for j in range(c):
        if 0<=j-1:
            dp[i][j] = max(dp[i][j], dp[i][j-1]+graph[i][j])
        if 0<=i-1:
            dp[i][j] = max(dp[i][j], dp[i-1][j] + graph[i][j])
        if 0<=j-1 and 0<=i-1:
            dp[i][j] = max(dp[i][j], dp[i - 1][j-1] + graph[i][j])

print(dp[r-1][c-1])