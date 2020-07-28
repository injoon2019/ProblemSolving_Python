'''
Problem Solving Baekjoon 11724
Author: Injun Son
Date: July 27, 2020
'''
import sys
sys.setrecursionlimit(10000)
from collections import deque

def dfs(v):
    visited[v] = True
    for e in arr[v]:
        if not visited[e]:
            dfs(e)

N, M = map(int, sys.stdin.readline().rstrip().split())
arr = [[] for _ in range(N+1)]
visited = [False] * (N+1)
count = 0

for _ in range(M):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    arr[a].append(b)
    arr[b].append(a)

for j in range(1, N+1):
    if not visited[j]:
        dfs(j)
        count +=1

print(count)
