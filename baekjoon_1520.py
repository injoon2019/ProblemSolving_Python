'''
Problem Solving Baekjoon 1520
Author: Injun Son
Date: November 19, 2020
'''
import sys

sys.setrecursionlimit(10**7)

dx = [-1, 0, 0, 1]
dy = [0, 1, -1, 0]

# dfs와 dp
# 상하좌우에 현재 자신의 위치보다 낮은 지점이 있을 경우 해당 지점들이 갖는 경로의 수의 합을 현재 위치에 합하도록 했다.
# 한 번 방문해서 경로의 수를 갖고있다면 그대로 반환하고, 방문한 적이 없던 지점이라면 새롭게 경로의 수를 구하게 된다.

def dfs(y, x):
    if y == n-1 and x == m-1:
        return 1
    rtn = 0
    for i in range(4):
        ny, nx = y+dy[i], x+dx[i]
        if 0<= ny < n and 0<= nx< m and graph[ny][nx] < graph[y][x]:
            if visited[ny][nx] >= 0:
                rtn += visited[ny][nx]
            else:
                rtn += dfs(ny, nx)
    visited[y][x] = rtn
    return rtn

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[-1]*m for _ in range(n)]
visited[0][0] = 0
print(dfs(0, 0))