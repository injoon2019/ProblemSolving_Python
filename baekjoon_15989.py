'''
Problem Solving Baekjoon 15989
Author: Injun Son
Date: September 22, 2020
'''
import sys
import copy
from itertools import combinations
from collections import deque

T = int(input())
dp = [[0,0,0,0] for _ in range(10001)]

#dp[i][1]은 합이 i인데 끝의 자리가 1인 경우의 수
dp[1][1] = 1
dp[2][1] = 1
dp[2][2] = 1

dp[3][1] = 1
dp[3][2] = 1
dp[3][3] = 1

for i in range(4, 10001):
    dp[i][1] = dp[i-1][1]
    dp[i][2] = dp[i-2][1] + dp[i-2][2]
    dp[i][3] = dp[i-3][1] + dp[i-3][2]+ dp[i-3][3]

for _ in range(T):
    n = int(input())
    print(sum(dp[n]))