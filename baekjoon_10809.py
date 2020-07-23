'''
Problem Solving Baekjoon 10809
Author: Injun Son
Date: July 23, 2020
'''
import sys

str = sys.stdin.readline().rstrip()
arr = [-1]*26
for i in range(len(str)):
    if arr[ord(str[i])-ord('a')]==-1:
        arr[ord(str[i])-ord('a')]=i

for i in range(len(arr)):
    print(arr[i], end=" ")