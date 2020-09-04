'''
Problem Solving Baekjoon 1697_3
Author: Injun Son
Date: August 15, 2020
'''
import sys
from collections import deque
sys.setrecursionlimit(100000)
MAX = 100001

visited = [0]*100001
N, K = map(int, input().split())

def bfs(N):
    q = deque()
    q.append([N, 0])
    visited[N] = True
    while q:
        v , cnt= q.popleft()
        visited[v] = True
        if v==K:
            print(cnt)
            exit()

        if v+1<=100000 and visited[v+1]==False:
            v1 = v+1
            q.append([v1, cnt+1])

        if v-1>=0 and visited[v-1]==False:
            v2 = v-1
            q.append([v2, cnt+1])

        if v*2<=100000 and visited[v*2]==False:
            v3 = v*2
            q.append([v3, cnt+1])

bfs(N)