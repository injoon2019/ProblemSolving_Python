'''
Problem Solving Baekjoon 1699_3
Author: Injun Son
Date: October 19, 2020
'''
import sys
sys.setrecursionlimit(100000)

N = int(input())
dp = [0]*100001
for i in range(100001):
    dp[i] = i
    for j in range(1, i):
        if j*j > i:
            break
        if dp[i]> dp[i- j*j]+1:
            dp[i] = dp[i- j*j] +1

print(dp[N])