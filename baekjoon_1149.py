'''
Problem Solving Baekjoon 1149
Author: Injun Son
Date: September 23, 2020
'''
import sys
import copy
from itertools import combinations
from collections import deque
import math

N = int(input())
cost = []
for _ in range(N):
    r, g, v = map(int, input().split())
    cost.append([r, g, v])

'''
dp[i][0] = i번째 집을 r로 칠할 때 최소 값 = cost[i][0]+ min(dp[i-1][1], dp[i-1][2] )
dp[i][1] = i번째 집을 g로 칠할 때 최소 값 = cost[i][1]+ min(dp[i-1][0], dp[i-1][2] )
dp[i][2] = i번째 집을 b로 칠할 때 최소 값 = cost[i][2]+ min(dp[i-1][0], dp[i-1][1] )

'''
dp = [ [0,0,0] for _ in range(N+1)]
dp[0][0] = cost[0][0]
dp[0][1] = cost[0][1]
dp[0][2] = cost[0][2]

for i in range(1, N):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2])+cost[i][0]
    dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + cost[i][1]
    dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + cost[i][2]

print(min(dp[N-1]))