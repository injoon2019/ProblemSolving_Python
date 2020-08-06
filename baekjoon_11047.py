'''
Problem Solving Baekjoon 11047
Author: Injun Son
Date: August 5, 2020
'''
n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
count = 0
for i in range(len(coins)-1, -1, -1):
    count += k//coins[i]
    k %= coins[i]

if k>0:
    print(-1)
else:
    print(count)