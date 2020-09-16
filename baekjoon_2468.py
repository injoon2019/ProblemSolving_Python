'''
Problem Solving Baekjoon 2468
Author: Injun Son
Date: September 16, 2020
'''
from collections import deque
import heapq
import sys, copy
sys.setrecursionlimit(100000)
N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
dx = [-1, 0, 0, 1]
dy = [0, 1, -1, 0]

max_rain = 0
max_safe = 0

for i in range(N):
    max_rain = max(max_rain, max(graph[i]))

def dfs(y, x, k):
    global visited_check
    for i in range(4):
        ny, nx = y+dy[i], x+dx[i]
        if 0<=nx<N and 0<=ny<N and graph[ny][nx]>k and visited_check[ny][nx]==0:
            visited_check[ny][nx]=1
            dfs(ny, nx, k)

for k in range(max_rain+1):
    visited_check = [[0] * N for _ in range(N)]
    region_count = 0
    for i in range(N):
        for j in range(N):
            if visited_check[i][j]==0 and graph[i][j]>k:
                region_count +=1
                visited_check[i][j] = 1
                dfs(i,j,k)

    max_safe = max(max_safe, region_count)

print(max_safe)