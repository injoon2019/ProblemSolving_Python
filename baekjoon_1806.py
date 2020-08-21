'''
Problem Solving Baekjoon 1806
Author: Injun Son
Date: August 21, 2020
'''
import sys

n, s = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

first, second = 0, 0
tmp = 0
min_length = sys.maxsize

while True:
    if tmp >= s:
        min_length = min(min_length, second-first)
        tmp -= arr[first]
        first +=1

    elif second == n:
        break

    else:
        tmp += arr[second]
        second+=1

if min_length == sys.maxsize:
    print(0)
else:
    print(min_length)


