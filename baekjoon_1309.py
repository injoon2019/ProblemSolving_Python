'''
Problem Solving Baekjoon 1309
Author: Injun Son
Date: September 23, 2020
'''
import sys
import copy
from itertools import combinations
from collections import deque
import math

N = int(input())
MOD = 9901
#dp[i][0] = i행에 아무것도 안두는 경우의 수
#dp[i][1] = i행에 왼쪽 칸에 두는 경우의 수
#dp[i][2] = i행에 오른쪽 칸에 두는 경우의 수

dp = [[1, 0, 0] for _ in range(N+1)]
dp[0][1] = 1
dp[0][2] = 1

for i in range(1, N):
    dp[i][0] = (dp[i-1][0]+ dp[i-1][1]+dp[i-1][2])%MOD
    dp[i][1] = (dp[i-1][0]+ dp[i-1][2]) % MOD
    dp[i][2] = (dp[i-1][0]+ dp[i-1][1]) % MOD

print(sum(dp[N-1])%MOD)