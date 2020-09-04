'''
Problem Solving Baekjoon 16964
Author: Injun Son
Date: August 15, 2020
'''
import sys
from collections import deque
sys.setrecursionlimit(100000)
MAX = 100001

N = int(input())
visited = [False]*(N+1)
visited[0] = True
visited_order2 = []



def all_visited():
    for i in range(1, N+1):
        if visited[i]==False:
            return False
    return True

graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, N+1):
    graph[i].sort()

visited_order = list(map(int, input().split()))
def dfs(v):
    global visited_order2
    visited[v]=True
    visited_order2.append(v)

    if all_visited():
        return visited_order2

    else:
        for adj_node in graph[v]:
            if visited[adj_node]==False:
                dfs(adj_node)


dfs(1)
if visited_order == visited_order2:
    print(1)
else:
    for i in range(1, N + 1):
        graph[i].sort(reverse=True)

    visited_order2 = []
    visited = [False] * (N + 1)
    visited[0] = True
    dfs(1)
    if visited_order == visited_order2:
        print(1)
    else:
        print(0)