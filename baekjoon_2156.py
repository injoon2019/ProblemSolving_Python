'''
Problem Solving Baekjoon 2156
Author: Injun Son
Date: July 16, 2020
'''

n = int(input())
arr = [0] + [int(input()) for _ in range(n)] + [0]
dp = [0]*(n+2)
'''
dp[n]을 n번째까지 최대값이라 할 때, 최대로 마실 수 있는 포도주의 양이라고 하면
세가지로 분류된다.
1. n번째 잔을 마시지 않은 경우: dp[n-1]
2. n번째 잔이 연속 1잔째 마신 경우: dp[n-2] + arr[n]
3. n번째 잔이 연속 2잔째 마신 경우: dp[n-3] + arr[n-1] + arr[n-1]
'''

dp[1], dp[2] = arr[1], arr[1]+arr[2]

for i in range(3, n+1):
    dp[i] = dp[i-1]
    dp[i] = max(dp[i], dp[i-2]+arr[i])
    dp[i] = max(dp[i], dp[i-3]+arr[i-1]+arr[i])


print(dp[n])