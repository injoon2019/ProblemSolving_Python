'''
Problem Solving Baekjoon 15990
Author: Injun Son
Date: September 16, 2020
'''
from collections import deque
import heapq
import sys, copy

MOD = 1000000009
T = int(input())
#dp[i] = [a,b,c] -> i를 1,2,3으로 나타내는데 끝 값이 1인 경우의 수 a, 끝 값이 2인 경우의 수 b, 끝 값이 3인 경우의 수 c
dp = [ [0,0,0] for _ in range(100001)]
dp[1] = [1,0,0]
dp[2] = [0,1,0]
dp[3] = [1,1,1]
for i in range(4, 100001):
    #1로 끝나는 경우
    dp[i][0] = ((dp[i-1][1]%MOD)+(dp[i-1][2]%MOD))%MOD

    #2로 끝나는 경우
    dp[i][1] = ((dp[i-2][0]%MOD)+(dp[i-2][2]%MOD))%MOD

    #3로 끝나는 경우
    dp[i][2] = ((dp[i-3][0]%MOD)+(dp[i-3][1]%MOD))%MOD


for _ in range(T):
    n = int(input())
    print(  (((dp[n][0]%MOD)+(dp[n][1]%MOD))%MOD +(dp[n][2]%MOD))%MOD )
