'''
Problem Solving Baekjoon 2491
Author: Injun Son
Date: August 26, 2020
'''
import math, sys

N = int(input())
arr = list(map(int, input().split()))
dp1 = [1]*N #i를 포함할때, 가장 긴 증가하는 수열
dp2 = [1]*N #가장 긴 감소하는 수열

for i in range(1, N):
    if arr[i] >= arr[i-1]:
        dp1[i] = dp1[i-1]+1
    #아니라면 연속이 끊기는 것이니, 기본 값인 1

for i in range(1, N):
    if arr[i] <= arr[i-1]:
        dp2[i] = dp2[i-1]+1

print(max(max(dp1), max(dp2)))