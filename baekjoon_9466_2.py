'''
Problem Solving Baekjoon 9466
Author: Injun Son
Date: July 28, 2020
'''
import sys
sys.setrecursionlimit(10000)
from collections import deque

T = int(sys.stdin.readline())
for _ in range(T):
    n = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().rstrip().split()))
    arr = [0]+arr
    visited = [[] for _ in range(n+1)]
    check = [0]*(n+1)
    grouped = []
    
    for i in range(1, len(arr)):
        v = i
        if check[i]==0:
            while v not in visited[i] and v not in grouped:
                visited[i].append(v)
                check[v]=1
                v = arr[v]
            repeat_start = visited[i].index(v)
            grouped += visited[i][repeat_start:]

    grouped = list(set(grouped))
    print(n - len(grouped))