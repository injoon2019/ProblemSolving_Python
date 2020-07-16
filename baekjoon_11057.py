'''
Problem Solving Baekjoon 11057
Author: Injun Son
Date: July 16, 2020
'''

N = int(input())

arr = [[0 for c in range(0,10)] for r in range(0,N+1)]
mod = 10007

for j in range(0,10):
    arr[1][j] = 1

for i in range(1, N+1):
    arr[i][0]=1

for i in range(2, N+1):
    for j in range(1,10):
        for k in range(0, j+1):
            arr[i][j] += (arr[i-1][k] % mod)

sum = 0
for j in range(0,10):
    sum += (arr[N][j] % mod)

print(sum%mod)