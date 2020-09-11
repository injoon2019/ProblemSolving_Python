'''
Problem Solving Baekjoon 13549
Author: Injun Son
Date: September 11, 2020
'''
import sys
from heapq import heappop, heappush
from collections import deque

N, K = map(int, input().split())

def bfs(start):
    q = deque()
    visited = dict()
    visited[start] = 0
    q.append(start)
    while q:
        v = q.popleft()
        if v==K:
            return visited[v]

        if 0<=v-1 and (v-1 not in visited.keys() or visited[v]+1 < visited[v-1]) :
            visited[v-1] = visited[v]+1
            q.append(v-1)
        if 0<=v+1<=110000 and (v+1 not in visited.keys() or visited[v]+1 < visited[v+1]) :
            visited[v+1] = visited[v]+1
            q.append(v+1)
        if 0<=v*2<=110000 and (v*2 not in visited.keys() or visited[v] < visited[v*2]) :
            visited[v*2] = visited[v]
            q.append(v*2)

print(bfs(N))



