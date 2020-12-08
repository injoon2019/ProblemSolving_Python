'''
Problem Solving Baekjoon 1520
Author: Injun Son
Date: November 19, 2020
'''
import sys

sys.setrecursionlimit(10**7)

dx = [-1, 0, 0, 1]
dy = [0, 1, -1, 0]

def dfs(y, x):
    if y==m-1 and x==n-1:
        return 1

    result = 0
    for k in range(4):
        ny, nx = y + dy[k], x + dx[k]
        if 0<=ny<m and 0<=nx<n and graph[ny][nx] < graph[y][x]:
            if visited[ny][nx] >= 0:
                result += visited[ny][nx]
            else:
                result += dfs(ny, nx)
    visited[y][x] = result
    return result

m, n  = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(m)]
visited = [[-1]*n for _ in range(m)]
visited[0][0] = 0
print(dfs(0,0))