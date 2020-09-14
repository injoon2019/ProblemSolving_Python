'''
Problem Solving Baekjoon 2003_4
Author: Injun Son
Date: September 14, 2020
'''
import sys

n, target = map(int, input().split())
arr = list(map(int, input().split()))

lo, high = 0,1
tmp = arr[lo]
cnt = 0

while lo < n:
    if high==n and tmp < target:
        break

    if target == tmp:
        cnt +=1
        tmp -= arr[lo]
        lo +=1

    elif tmp < target:
        tmp += arr[high]
        high +=1

    elif tmp > target:
        tmp -= arr[lo]
        lo +=1

print(cnt)