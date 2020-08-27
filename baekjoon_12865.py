'''
Problem Solving Baekjoon 12865
Author: Injun Son
Date: August 27, 2020
'''
import sys

N, K = map(int, input().split())
weights = []
values = []
for _ in range(N):
    weight, value = map(int, input().split())
    weights.append(weight)
    values.append(value)

weights = [0]+weights
values = [0]+values

dp = [ [0 for i in range(K+1)] for _ in range(N+1)]
#dp[i][j] = 남은 체력이 j이고, i번째 아이템까지 검사하는 경우

for i in range(1, N+1):
    for j in range(0, K+1):
        if j - weights[i] >=0:
            dp[i][j] = max(dp[i-1][j], values[i]+dp[i-1][j-weights[i]])
        else:
            dp[i][j] = dp[i-1][j]

ans = -1*sys.maxsize
for i in range(N+1):
    ans = max(ans, max(dp[i]))
print(ans)