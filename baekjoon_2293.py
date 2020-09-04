'''
Problem Solving Baekjoon 2293
Author: Injun Son
Date: September 3, 2020
'''
from collections import deque
import sys

import sys
n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
dp = [0]*(k+1)
dp[0] =1

for coin in coins:
    for j in range(coin, k+1):
        if j-coin >=0:
            dp[j] += dp[j-coin]
print(dp[k])
