'''
Problem Solving Baekjoon 1535
Author: Injun Son
Date: August 26, 2020
'''
import sys
from collections import deque
from itertools import combinations
from itertools import permutations
import math
sys.setrecursionlimit(100000)
#https://dheldh77.tistory.com/232

N= int(input())
weight = list(map(int, input().split()))
value = list(map(int, input().split()))
dp = [[0 for i in range(101)] for _ in range(21)]
# dp[i][j] = 행 i 는 물건 i까지 넣을 수 있을 때를 의미하고, 열 j는 가방의 최대 무게를 의미한다.
ans = 0
for i in range(N):
    for j in range(100):
        if weight[i-1] <=j:
            dp[i][j] = max(value[i-1]+dp[i-1][j-weight[i-1]], dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]
        ans = max(dp[i][j], ans)

print(ans)
