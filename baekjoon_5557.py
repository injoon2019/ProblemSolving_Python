'''
Problem Solving Baekjoon 5557
Author: Injun Son
Date: September 17, 2020
'''
import sys
from collections import deque

n = int(input())
arr = list(map(int, input().split()))
dp = [[0]*21 for _ in range(n)]
#dp[i][j] = i번째까지 j를 만드는 방법의 수
dp[0][arr[0]] = 1
for i in range(1, n):
    cur = arr[i]
    for j in range(0, 21):
        if dp[i-1][j] != 0:
            if 0<=j-cur<=20:
                dp[i][j-cur] += dp[i-1][j]
            if 0<= j+cur<=20:
                dp[i][j+cur] += dp[i-1][j]

# for i in range(n):
#     print(i, dp[i], sum(dp[i]))
# print()
# print(dp[n-2])
print(dp[n-2][arr[n-1]])