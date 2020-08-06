'''
Problem Solving Baekjoon 2294
Author: Injun Son
Date: August 5, 2020
'''
n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
coins.sort()
count = 0
for i in range(len(coins)-1, -1, -1):
    count += n//coins[i]
    n %= coins[i]

if n>0:
    print(-1)
else:
    print(count)