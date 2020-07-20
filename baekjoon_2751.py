'''
Problem Solving Baekjoon 2751
Author: Injun Son
Date: July 20, 2020
'''

N = int(input())
arr = [int(input()) for _ in range(N)]
arr.sort()
for i in arr:
    print(i)