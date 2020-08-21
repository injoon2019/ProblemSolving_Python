'''
Problem Solving Baekjoon 2003
Author: Injun Son
Date: August 21, 2020
'''
import sys

n, target = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

cnt = 0
lo, hi = 0, 1
tmp = arr[lo]
while lo < n:
    if tmp == target:
        cnt +=1
        tmp -= arr[lo]
        lo +=1

    if hi==n and tmp< target:
        break
    elif tmp < target:
        tmp += arr[hi]
        hi +=1
    elif tmp > target:
        tmp-=arr[lo]
        lo+=1

print(cnt)