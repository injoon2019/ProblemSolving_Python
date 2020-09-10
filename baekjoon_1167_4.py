'''
Problem Solving Baekjoon 1167_3
Author: Injun Son
Date: September 10, 2020
'''
import sys
from heapq import heappop, heappush
INF = sys.maxsize

V = int(input())

graph = [[] for _ in range(V+1)]
for i in range(1, V+1):
    arr = list(map(int, input().split()))
    for j in range(1, len(arr)-1, 2):
        graph[arr[0]].append([arr[j], arr[j+1]])

def print_board():
    for i in range(V+1):
        for j in range(V+1):
            print(graph[i][j], end=" ")
        print()

def dijkstra(start):
    v = start
    heap = []
    d = [INF]*(V+1)
    d[v] = 0
    heappush(heap, [0, start])
    while heap:
        weight, node = heappop(heap)
        for new_node, new_weight in graph[node]:
            new_weight2 = weight+new_weight
            if d[new_node]> new_weight2:
                d[new_node] = new_weight2
                heappush(heap, [new_weight2, new_node])
    return d

arr = dijkstra(1)
arr2 = dijkstra(arr.index(max(arr[1:])))
print(max(arr2[1:]))