'''
Problem Solving Baekjoon 1922
Author: Injun Son
Date: September 1, 2020
'''
import math, sys
import heapq

def prim(start_node):
    visited = [False]*(N+1)
    visited[start_node] = True
    heap = []
    for adj_node in graph[start_node]:
        heapq.heappush(heap, adj_node)
    node_count = 1
    distance_sum = 0
    while heap:
        d,v = heapq.heappop(heap)
        if not visited[v]:
            visited[v] = True
            node_count +=1
            distance_sum += d
            for adj_node in graph[v]:
                heapq.heappush(heap, adj_node)

        if node_count==N:
            return distance_sum

    return 0

N = int(input())
M = int(input())
graph = [ [] for _ in range(N+1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append([c, b])
    graph[b].append([c, a])

print(prim(1))