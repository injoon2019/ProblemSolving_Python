'''
Problem Solving Baekjoon 1389
Author: Injun Son
Date: August 27, 2020
'''
import sys
from heapq import heappop, heappush

N, M = map(int, input().split())
#N명의 사람이 있다
graph = [[] for _ in range(N+1)]
ans_list = [[] for _ in range(N+1)]
INF = sys.maxsize

def dijkstra(start):
    heap = []
    d = [INF for _ in range(N+1)]
    d[start] = 0
    heappush(heap, [start, 0])
    while heap:
        node, weight = heappop(heap)
        for new_nodes in graph[node]:
            new_node, new_weight = new_nodes, 1
            if d[new_node] > d[node]+new_weight:
                d[new_node] = d[node] + new_weight
                heappush(heap, [new_node, new_weight])

    return d

def get_sum(tlst):
    lst= tlst[0]
    sum = 0
    for i in range(1, len(lst)):
        sum += lst[i]
    return sum

for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    graph[B].append(A)

for i in range(1, N+1):
    ans_list[i].append(dijkstra(i))

ans = 1
min_val = sys.maxsize

for i in range(1, len(ans_list)):
    if get_sum(ans_list[i]) < min_val:
        min_val = get_sum(ans_list[i])
        ans = i
print(ans)