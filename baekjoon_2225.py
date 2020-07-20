'''
Problem Solving Baekjoon 2225
Author: Injun Son
Date: July 19, 2020
'''
#https://mygumi.tistory.com/135

N, K = map(int, input().split())
dp = [[0]*201 for r in range(201)]
#dp[K][N] = 0부터 N까지의 정수 K개를 더해서 그 합이 N이 되는 경우
#마지막에 고를 수 있는 수 L (0 <= L <=N)
#dp[K][N] = sum( dp[K-1][N-L]
for i in range(N+1):
    dp[1][i] = 1

for i in range(1, K+1):
    for j in range(0,N+1):
        for l in range(0,j+1):
            dp[i][j] += dp[i-1][j-l]
            dp[i][j] %= 1000000000

#print(dp)
print(dp[K][N])