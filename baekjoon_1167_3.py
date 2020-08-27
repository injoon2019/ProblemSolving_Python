'''
Problem Solving Baekjoon 1167_3
Author: Injun Son
Date: August 27, 2020
'''
import sys
from heapq import heappop, heappush
INF = sys.maxsize


def dijkstra(start):
    heap = []
    heappush(heap, [0, start])
    d = [INF for _ in range(N+1)]
    d[start] = 0
    while heap:
        weight, node = heappop(heap)
        for new_node, new_weight in graph[node]:
            new_weight2 =weight + new_weight
            if d[new_node] > new_weight2:
                d[new_node] = new_weight2
                heappush(heap, [new_weight2, new_node])

    return d


N = int(input())
graph = [[] for _ in range(N+1)]
for i in range(1, N+1):
    a = list(map(int, input().split()))
    for j in range(1, len(a)-1, 2):
        graph[a[0]].append([a[j], a[j+1]])

ans = dijkstra(1)
print(max(dijkstra(ans.index(max(ans[1:])))[1:]))