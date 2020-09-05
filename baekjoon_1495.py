'''
Problem Solving Baekjoon 1495
Author: Injun Son
Date: September 4, 2020
'''
from collections import deque
import sys
from itertools import combinations

N, S, M  = map(int, input().split())
V = list(map(int, input().split()))

#모든 볼륨에 관해 연주 가능 여부를 계산하기
dp = [ [0]*(M+1) for _ in range(N+1)]
#dp[N][S] = N번째 곡일 때, 볼륨 S 가능 여부
dp[0][S] = 1

for i in range(1, N+1):
    for j in range(M+1):

        if dp[i-1][j]==0:
            continue
        if j + V[i-1] <=M:
            dp[i][j+V[i-1]] = 1
        if j - V[i-1] >=0:
            dp[i][j-V[i-1]] = 1

ans = -1
for i in range(M, -1, -1):
    if dp[-1][i]==1:
        ans = i
        break
print(ans)