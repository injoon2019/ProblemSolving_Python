'''
Problem Solving Baekjoon 1197_2
Author: Injun Son
Date: October 1, 2020
'''
import math, sys
import heapq

def prim(start_node):
    visited = [False]*(V+1)
    visited[start_node] = True
    heap = []
    node_count = 1
    distance_sum = 0

    for a in graph[start_node]:
        heapq.heappush(heap, a)

    while heap:
        w, v = heapq.heappop(heap)
        if visited[v] == False:
            distance_sum += w
            node_count +=1
            visited[v] = True
            for adj_node in graph[v]:
                heapq.heappush(heap, adj_node)

        if node_count == V:
            return distance_sum
    return 0

V, E = map(int, input().split())
graph = [ [] for _ in range(V+1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    #가중치 c로 b와 연결되어있다
    graph[a].append((c, b))
    graph[b].append((c, a))

print(prim(1))