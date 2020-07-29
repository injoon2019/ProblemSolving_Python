'''
Problem Solving Baekjoon 1920
Author: Injun Son
Date: July 29, 2020
'''
import sys
from collections import deque
sys.setrecursionlimit(100000)

N = int(input())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
M = int(input())
arr1 = list(map(int, sys.stdin.readline().rstrip().split()))
arr.sort()
for i in arr1:
    if i in arr:
        print(1)
    else:
        print(0)
