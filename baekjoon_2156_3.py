'''
Problem Solving Baekjoon 2156_3
Author: Injun Son
Date: August 25, 2020
'''

n = int(input())
arr = [0]+[int(input()) for _ in range(n)]+[0]
dp = [0]*(n+2)
dp[1] = arr[1]
dp[2] = arr[2]+arr[1]
for i in range(3, n+2):
    #dp[i]가 연속 2잔째 일 때,
    dp[i] = max(dp[i], dp[i-3]+arr[i-1]+arr[i])
    #dp[i]가 연속 1잔째 일 때,
    dp[i] = max(dp[i], dp[i-2]+arr[i])
    #dp[i]가 연속 0잔째 일 때,
    dp[i] = max(dp[i], dp[i-1])

print(max(dp))

