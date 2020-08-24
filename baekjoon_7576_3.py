'''
Problem Solving Baekjoon 7576_3
Author: Injun Son
Date: August 24, 2020
'''
import sys
from collections import deque
sys.setrecursionlimit(100000)

dx = [-1, 0, 0, 1]
dy = [0, 1, -1, 0]

c, r = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(r)]
visited_check = [[0]*c for _ in range(r)]
def bfs():
    global count
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if 0<=nx<c and 0<=ny<r:
                if visited_check[ny][nx] ==0 and graph[ny][nx]==0:
                    graph[ny][nx]=graph[y][x]+1
                    visited_check[ny][nx]=1
                    q.append([ny, nx])


q = deque()
for i in range(r):
    for j in range(c):
        if graph[i][j]==1:
            q.append([i, j])
            visited_check[i][j]=1
count = 0
bfs()
max_day = 0

for i in range(r):
    for j in range(c):
        if graph[i][j]==0:
            print(-1)
            exit()
        else:
            if graph[i][j]> max_day:
                max_day = graph[i][j]

# for i in range(r):
#     for j in range(c):
#         print(graph[i][j], end=" ")
#     print()
print(max_day-1)