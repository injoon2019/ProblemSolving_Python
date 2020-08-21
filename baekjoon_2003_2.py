'''
Problem Solving Baekjoon 2003_2
Author: Injun Son
Date: August 21, 2020
'''
import sys

n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

cnt= 0
low, high = 0, 1
tmp = arr[low]

while low < n:
    if tmp == m:
        cnt +=1
        tmp -= arr[low]
        low +=1

    if high==n and tmp < m:
        break

    elif tmp < m:
        tmp += arr[high]
        high +=1

    elif tmp > m:
        tmp -= arr[low]
        low+=1

print(cnt)




