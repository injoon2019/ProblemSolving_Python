'''
Problem Solving Baekjoon 11727
Author: Injun Son
Date: July 15, 2020
'''
n = int(input())
arr = [0]*(1001)

arr[1] = 1
arr[2] = 3

for i in range(3, 1001):
    arr[i] = (arr[i-1]%10007 + (2*arr[i-2])%10007)%10007

print(arr[n])
