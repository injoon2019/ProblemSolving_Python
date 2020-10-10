'''
Problem Solving Baekjoon 2075
Author: Injun Son
Date: October 10, 2020
'''
import sys
sys.setrecursionlimit(100000)
from queue import PriorityQueue

n = int(input())

d = list(map(int, input().split()))

for i in range(n-1):
    temp  = sorted(list(map(int, input().split()))+ d, reverse=True)
    d = temp[:n]

print(d[n-1])