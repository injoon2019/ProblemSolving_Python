'''
Problem Solving Baekjoon 1260_2
Author: Injun Son
Date: August 24, 2020
'''
import sys
from collections import deque

N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]

def DFS(V):
    if len(ans)==N:
        return

    if V not in ans:
        ans.append(V)

    for node in graph[V]:
        if node not in ans:
            DFS(node)

def BFS(V):
    q = deque([V])
    ans.append(V)
    while q:
        v = q.popleft()
        for node in graph[v]:
            if node not in ans:
                ans.append(node)
                q.append(node)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, N+1):
    graph[i].sort()

ans = []
DFS(V)
print(' '.join(map(str, ans)))
ans = []
BFS(V)
print(' '.join(map(str, ans)))