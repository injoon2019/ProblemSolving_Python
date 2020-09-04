'''
Problem Solving Baekjoon 1890
Author: Injun Son
Date: September 3, 2020
'''
from collections import deque
import sys

import sys
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
dp = [ [0]*n for _ in range(n)]

dp[0][0] = 1

def print_board():
    for i in range(n):
        for j in range(n):
            print(dp[i][j], end=" ")
        print()
    print()

for i in range(n):
    for j in range(n):
        if i==n-1 and j==n-1:
            break
        if i+graph[i][j]<n:
            dp[i+graph[i][j]][j] += dp[i][j]
            # print(i, j)
            # print_board()

        if j+graph[i][j]<n:
            dp[i][j+graph[i][j]] += dp[i][j]
            # print(i, j)
            # print_board()

print(dp[n-1][n-1])