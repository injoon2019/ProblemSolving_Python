'''
Problem Solving Baekjoon 10989
Author: Injun Son
Date: July 20, 2020
'''
import sys

N = int(input())
arr = [0]*10001

for i in range(N):
    x = int(sys.stdin.readline())
    arr[x]+=1

for i in range(1, 10001):
    if arr[i]!=0:
        for c in range(arr[i]):
            print(i)