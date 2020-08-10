'''
Problem Solving Baekjoon 10815
Author: Injun Son
Date: August 10, 2020
'''
import sys
import math
M = int(input())
arr = list(map(int, input().split()))
N = int(input())
arr2 = list(map(int, input().split()))
arr.sort()
for i in arr2:
    start = 0
    end = len(arr)-1
    mid = (start+end)//2
    isThere = False
    while start<=end:
        if arr[mid]==i:
            isThere=True
            break
        elif arr[mid] < i:
            start = mid +1
        elif arr[mid]> i:
            end = mid -1
        mid = (start + end) // 2
    if isThere:
        print("1", end= " ")
    else:
        print("0", end= " ")
