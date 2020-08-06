'''
Problem Solving Baekjoon 1920_2
Author: Injun Son
Date: August 6, 2020
'''
import sys
from collections import deque
sys.setrecursionlimit(100000)

def binary_search(i):
    start = 0
    end = len(arr)-1
    mid = (start+end)//2
    while start <= end:
        if arr[mid]== i:
            return True
        elif arr[mid] < i:
            start = mid +1
        elif arr[mid] > i:
            end = mid -1
        mid = (start + end) // 2

    return False

N = int(input())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
M = int(input())
arr1 = list(map(int, sys.stdin.readline().rstrip().split()))
arr.sort()
for i in arr1:
    if binary_search(i):
        print(1)
    else:
        print(0)
