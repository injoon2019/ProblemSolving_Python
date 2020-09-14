'''
Problem Solving Baekjoon 14002
Author: Injun Son
Date: September 14, 2020
'''
from collections import deque
import heapq
import sys

N = int(input())
arr = list(map(int, input().split()))
dp = [1]*N
#dp[i] = i번째 원소까지 가장 긴 증가하는 수열의 길이
ans = ['']*N
for i in range(N):
    ans[i] = str(arr[i])

ans[0] = str(arr[0])
for i in range(1, N):
    for j in range(i):
        if arr[i] > arr[j]:
            if dp[i] < dp[j]+1:
                dp[i] = dp[j]+1
                ans[i] = ans[j]+' '+str(arr[i])

# print(dp)
# print(ans)
print(max(dp))
print(ans[dp.index(max(dp))])