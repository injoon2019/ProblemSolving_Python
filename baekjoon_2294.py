'''
Problem Solving Baekjoon 2294
Author: Injun Son
Date: August 27, 2020
'''
import sys
n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
#dp[i] = i를 만들때 쓰는 동전의 최소 개수
dp = [sys.maxsize-1]*(100000+1)
for coin in coins:
    dp[coin] = 1

for i in range(1, k+1):
    for coin in coins:
        if i-coin>0:
            if dp[i-coin]+1 < dp[i]:
                dp[i] = dp[i-coin]+1

if dp[k]== sys.maxsize-1:
    print(-1)
else:
    print(dp[k])

'''
동전이 배수 관계가 아니니 그리디하게 풀지 못한다

1. 런타임 에러들이 났던 이유 1: dp[i-coin]에서 i-coin이 음수가 될 수도 있다
2. coin이 K보다 클 수도 있다. dp를 k+1 사이즈로 선언해 놓으면, dp[coin[=1에서 
인덱스 초과날 수도 있다. 
'''