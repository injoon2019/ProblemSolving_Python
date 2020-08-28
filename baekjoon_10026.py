'''
Problem Solving Baekjoon 10026
Author: Injun Son
Date: August 28, 2020
'''
import math, sys, copy
from collections import deque
sys.setrecursionlimit(10**6)
dx = [-1, 0, 0, 1]
dy = [0, 1, -1, 0]

N = int(input())
graph = [list(input()) for _ in range(N)]
graph2 = copy.deepcopy(graph)
visited_check = [[0]*N for _ in range(N)]
visited_check2 = [[0]*N for _ in range(N)]
count1, count2 =0, 0

def bfs(y, x):
    q = deque()
    visited_check[y][x]=1
    q.append([y, x])
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if 0<=nx<N and 0<=ny<N:
                if visited_check[ny][nx]==0 and graph[y][x]==graph[ny][nx]:
                    visited_check[ny][nx]=1
                    q.append([ny, nx])

def dfs(y, x):
    visited_check2[y][x]=1
    for i in range(4):
        ny, nx = y+dy[i], x+dx[i]
        if 0<=nx<N and 0<=ny<N:
            if visited_check2[ny][nx]==0 and graph2[ny][nx]==graph2[y][x]:
                dfs(ny, nx)

#적록색약 사람 그래프를 아예 바꿔서 시작한다
for i in range(N):
    for j in range(N):
        if graph2[i][j]=='G':
            graph2[i][j]='R'

for i in range(N):
    for j in range(N):
        if visited_check[i][j]==0:
            count1 +=1
            bfs(i, j)

for i in range(N):
    for j in range(N):
        if visited_check2[i][j]==0:
            count2 +=1
            dfs(i, j)

print(count1, count2)
