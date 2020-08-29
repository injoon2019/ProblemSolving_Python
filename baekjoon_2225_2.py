'''
Problem Solving Baekjoon 2225_2
Author: Injun Son
Date: August 29, 2020
'''
MOD = 1000000000
N, K = map(int, input().split())
# dp[K][N] = K개의 정수를 더해서 0이 되는 경우
dp = [[0]*(N+1) for _ in range(K+1)]

#dp[1][0]=1, dp[2][0]=1, dp[3][0]=1 ...
for i in range(N+1):
    dp[1][i] = 1

for k in range(1, K+1):
    for n in range(0, N+1):
        tmp = 0
        for i in range(0, n+1):
            dp[k][n] += dp[k-1][n-i]
            dp[k][n] %= MOD

print(dp[K][N])
'''
dp[K][N] = dp[K-1][N-0] + dp[1][0]
         + dp[K-1][N-1] + dp[1][1]
         + dp[K-1][N-2] + dp[1][2]
         + dp[K-1][N-3] + dp[1][3]
         ..
         + dp[K-1][0] + dp[1][N]
'''