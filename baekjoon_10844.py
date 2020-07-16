'''
Problem Solving Baekjoon 10844
Author: Injun Son
Date: July 16, 2020
'''
N = int(input())
mod = 1000000000

#arr[n][x] = 길이가 n인 수에서 수x의 개수?
arr = [[0 for x in range(10)] for y in range(N+1) ]  # (N+1) x 10 배열
for i in range(1,10):
    arr[1][i] = 1

for i in range(2, N+1):
    for j in range(0, 10):
        if j>0 and j<9:
            arr[i][j] = ((arr[i-1][j-1] % mod)+ (arr[i-1][j+1] % mod))%mod
        elif j==0:
            arr[i][j] = arr[i-1][j+1] % mod
        elif j==9:
            arr[i][j] = arr[i-1][j-1] % mod

sum = 0
for i in range(10):
    sum = ((sum%mod)+(arr[N][i]%mod))%mod

print(sum)

'''
How to make 2d array in Python
'''
