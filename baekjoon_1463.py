'''
Problem Solving Baekjoon 1463
Author: Injun Son
Date: July 15, 2020
'''
n = int(input())
d = [0]*(n+1)

d[1] = 0

for i in range(2, n+1):
    d[i] = d[i-1] + 1
    if i%2 ==0 and d[i] > d[i//2]+1:
        d[i] = d[i//2]+1

    if i%3 ==0 and d[i] > d[i//3]+1:
        d[i] = d[i//3] + 1

print(d[n])

'''
파이썬에서 다른 언어에서의 array 쓰듯 길이 n 배열 선언하려면
arr = [0]*(n)
'''
