'''
Problem Solving Baekjoon 1260_2
Author: Injun Son
Date: July 27, 2020
'''
import sys
from collections import deque

def dfs():
    visited = []
    stack = [V]
    check = [0 for _ in range(N+1)]
    while stack:
        n = stack.pop()

        if not check[n]:
            visited.append(n)
            check[n]=1
            stack += graph[n]

    return visited

def bfs():
    visited =[]
    queue = deque([V])
    check = [0 for _ in range(N+1)]

    while queue:
        n = queue.popleft()

        if not check[n]:
            visited.append(n)
            check[n] = 1
            queue += reversed(graph[n])

    return visited


N, M, V = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for e in graph:
    e.sort(reverse=True)

print(' '.join(map(str, dfs())))
print(' '.join(map(str, bfs())))

