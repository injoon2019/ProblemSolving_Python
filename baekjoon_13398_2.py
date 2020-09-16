'''
Problem Solving Baekjoon 13398
Author: Injun Son
Date: September 16, 2020
'''
from collections import deque
import heapq
import sys, copy

input=  sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
dp = [ [0,0] for i in range(n)]
#dp[i][0] = i번째까지 숫자를 제외하지않고 최대연속합
#dp[i][1] = i번째까지 숫자를 한번 제외하고 최대 연속합 (제외 숫자는 arr[i]일 수도 있고 아닐수도 있다)
dp[0][0] = arr[0]

m = -sys.maxsize

if n>1:
    for i in range(1, n):
        dp[i][0] = max(dp[i-1][0]+arr[i], arr[i])
        dp[i][1] = max(dp[i-1][0], dp[i-1][1]+arr[i])
        m= max(m, dp[i][0], dp[i][1])
    print(m)
else:
    print(dp[0][0])