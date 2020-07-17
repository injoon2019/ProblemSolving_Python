'''
Problem Solving Baekjoon 11055
Author: Injun Son
Date: July 17, 2020
'''
import copy

N = int(input())
arr = list(map(int, input().split()))
dp = copy.deepcopy(arr)

#dp[i] = i를 선택하고,i까지 합이 가장 큰 증가 부분 수열의 합
for i in range(1,N):
    for j in range(0,i):
        #print(i, j)
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j]+arr[i])

print(max(dp))

