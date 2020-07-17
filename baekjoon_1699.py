'''
Problem Solving Baekjoon 1699
Author: Injun Son
Date: July 17, 2020
'''
import math

N = int(input())

arr = [0]*100001
dp = [0]*100001

#dp[i] = 숫자 i를 제곱수들의 합으로 나타낼 수 있는 촤소개수
for i in range(1, N+1):
    dp[i] = i
    for j in range(1, i):
        if j*j > i:
            break
        if dp[i]> dp[i-j*j]+1:
            dp[i] = dp[i-j*j]+1

print(dp[N])