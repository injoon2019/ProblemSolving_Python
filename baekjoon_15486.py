'''
Problem Solving Baekjoon 15486
Author: Injun Son
Date: September 6, 2020
'''
import sys

input = sys.stdin.readline
N = int(input())
arr = []
#dp[i] = i일에 상담을 할때 맥시멈? 상담 안하면 그 이전에 맥시멈?
dp = [0]*(N+1)
for _ in range(N):
    t, p = map(int, input().split())
    arr.append([t, p])

tmp_max = 0
for i in range(N):
    tmp_max = max(tmp_max, dp[i])
    if i+arr[i][0] > N:
        continue
    dp[i+arr[i][0]] = max(tmp_max+arr[i][1], dp[i+arr[i][0]])

print(max(dp))