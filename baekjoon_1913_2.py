'''
Problem Solving Baekjoon 1913
Author: Injun Son
Date: August 26, 2020
'''
import math, sys, copy
# 아래 오른 위 왼
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

n = int(input())
target = int(input())

graph = [[0]*n for _ in range(n)]
y, x = 0, 0
num = n*n
d = 0
while num > 0:
    if graph[y][x] != 0:
        break
    graph[y][x] = num

    ny, nx = y+dy[d], x+dx[d]
    if 0<=nx<n and 0<=ny<n and graph[ny][nx]==0:
        y, x = ny, nx

    else:
        d = (d+1)%4
        y, x = y+dy[d], x+dx[d]

    num -= 1

for i in range(n):
    for j in range(n):
        print(graph[i][j], end=" ")
        if graph[i][j]==target:
            ans = (i+1, j+1)
    print("")

print(ans[0], ans[1])


