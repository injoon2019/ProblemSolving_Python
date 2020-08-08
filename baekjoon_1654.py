'''
Problem Solving Baekjoon 1654
Author: Injun Son
Date: August 8, 2020
'''
import sys
import math

def check_count(val):
    count = 0
    for i in arr:
        count += (i // val)
    return count

def binary_search(min_val, max_val):
    global answer
    min = min_val
    max = max_val
    mid = (min+max)//2
    while min <= max:
        if check_count(mid)>=N:
            if mid > answer:
                answer = mid
                min = mid+1

        elif check_count(mid) < N:
            max = mid-1

        mid = (min + max) // 2

answer = 0
K, N = map(int, input().split())
arr = [int(input()) for _ in range(K)]
min_val = max(arr)
binary_search(1, min_val)
print(answer)