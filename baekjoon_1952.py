'''
Problem Solving Baekjoon 1952
Author: Injun Son
Date: August 26, 2020
'''
import math, sys
# 오 밑 왼 윗
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

r, c = map(int, input().split())
graph = [[0]*c for _ in range(r)]
y, x = 0, 0
d= 0
count = 1
ans = 0
while True:
    if graph[y][x]> 0:
        break
    graph[y][x] = count
    count +=1
    ny, nx = y + dy[d], x + dx[d]

    if 0<=ny<r and 0<=nx<c and graph[ny][nx]==0:
        pass
    else:
        d= (d+1)%4
        nx = x+dx[d]
        ny = y+dy[d]
        ans +=1

    y, x = ny, nx

# for i in range(r):
#     for j in range(c):
#         print(graph[i][j], end=" ")
#     print("")
print(ans-1)
