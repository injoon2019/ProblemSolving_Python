'''
Problem Solving Baekjoon 11053
Author: Injun Son
Date: July 17, 2020
'''
'''
7
8 9 10 1 2 3 4
'''
N = int(input())
arr = list(map(int, input().split()))
dp = [1]*N

for i in range(1, N):
    for j in range(0,i):
        if arr[i] > arr[j]:
            dp[i]= max(dp[i], dp[j]+1)

print(max(dp))