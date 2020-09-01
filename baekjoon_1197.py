'''
Problem Solving Baekjoon 1197
Author: Injun Son
Date: October 1, 2020
'''
import math, sys
import heapq

V, E = map(int, input().split())
adj = [ [] for _ in range(V+1)]

def prim(v):
    q = []
    visited = [False]*(V+1)
    visited[v] = True
    d = 0
    cnt = 1
    for a in adj[v]:
        heapq.heappush(q, a)

    while q:
        c, v = heapq.heappop(q)
        if not visited[v]:
            visited[v] = True
            cnt +=1
            d +=c
            for a in adj[v]:
                heapq.heappush(q, a)
        if cnt==V:
            return d
    return 0

for _ in range(E):
    a, b, c = map(int, input().split())
    adj[a].append((c, b))
    adj[b].append((c, a))

print(prim(1))

'''
프림 알고리즘
'''