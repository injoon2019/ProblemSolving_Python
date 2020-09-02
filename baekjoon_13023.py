'''
Problem Solving Baekjoon 13023
Author: Injun Son
Date: September 2, 2020
'''
import sys
import heapq
visited = []
def dfs(i, count):
    visited
    if count == 5:
        print("1")
        exit()

    for adj_node in graph[i]:
        if adj_node not in visited:
            visited.append(adj_node)
            dfs(adj_node, count+1)
            visited.remove(adj_node)

N, M = map(int, input().split())
graph = [ [] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(N):
    visited = [i]
    dfs(i, 1)
print("0")