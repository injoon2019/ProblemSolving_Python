'''
Problem Solving Baekjoon 10989
Author: Injun Son
Date: July 20, 2020
'''

N = int(input())
arr = [int(input()) for _ in range(N)]
arr.sort()
for i in range(len(arr)):
    print(arr[i])