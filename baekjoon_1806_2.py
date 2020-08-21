'''
Problem Solving Baekjoon 1806_2
Author: Injun Son
Date: August 21, 2020
'''
import sys

n, s = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

left, right = 0,0
tmp = 0
min_length = sys.maxsize
while True:
    if tmp>=s:
        min_length = min(min_length, right-left)
        tmp -= arr[left]
        left +=1

    elif right==n:
        break

    else:
        tmp += arr[right]
        right+=1

if min_length == sys.maxsize:
    print(0)
else:
    print(min_length)
