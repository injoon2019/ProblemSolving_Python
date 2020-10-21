'''
Problem Solving Baekjoon 1535_2
Author: Injun Son
Date: October 21, 2020
'''
import sys
from collections import deque
from itertools import combinations
from itertools import permutations
import math
sys.setrecursionlimit(100000)

N = int(input())
weight = list(map(int, input().split()))
value = list(map(int, input().split()))
#dp[i][j] = 물건 i까지 검사하고 무게 j까지
dp = [[0]*101 for _ in range(21)]
ans = 0

for i in range(N):
    for j in range(100):
        if weight[i-1] <= j:
            dp[i][j] = max(value[i-1]+dp[i-1][j-weight[i-1]], dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]
        ans = max(ans, dp[i][j])

print(ans)