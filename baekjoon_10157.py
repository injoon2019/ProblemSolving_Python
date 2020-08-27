'''
Problem Solving Baekjoon 10157
Author: Injun Son
Date: August 26, 2020
'''
import math, sys
# 위 오른 아래 왼
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
c, r = map(int, input().split())
K = int(input())
graph = [[0]*c for _ in range(r)]
num =1
y, x = r-1, 0
d = 0
while num<= r*c:
    graph[y][x] = num
    ny, nx = y+dy[d], x+dx[d]
    if 0<=nx<c and 0<=ny<r and graph[ny][nx]==0:
        y, x = ny, nx
        if graph[y][x]!=0:
            break
    else:
        d = (d+1)%4
        y, x = y+dy[d], x+dx[d]
        if graph[y][x]!=0:
            break

    num+=1
ans = (-1,-1)
for i in range(r):
    for j in range(c):
        # print(graph[i][j], end=" ")
        if graph[i][j] == K:
            ans = (i, j)
            # print(ans)
    # print("")

if ans[0]==-1 and ans[1]==-1:
    print(0)
else:
    print(ans[1]+1, abs(ans[0]-r))
