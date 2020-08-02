'''
Problem Solving Baekjoon 2146
Author: Injun Son
Date: Aug 2, 2020
'''
import sys
sys.setrecursionlimit(10**6)
from collections import deque

n = int(input())
a = [list(map(int, input().split())) for i in range(n)]
check = [[False]*n for _ in range(n)]
dx = [-1, 0, 0, 1]
dy = [0, 1, -1, 0]
ans =sys.maxsize
k= 1

def dfs(x,y):
    check[x][y] = True
    a[x][y] = k
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0<=nx<n and 0<=ny<n:
            if not check[nx][ny] and a[nx][ny]:
                dfs(nx, ny)

def bfs(z):
    global ans
    dist = [[-1]*n for _ in range(n)]
    q = deque()
    for i in range(n):
        for j in range(n):
            if a[i][j]==z:
                q.append((i, j))
                dist[i][j] = 0

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=n:
                continue
            if a[nx][ny] and a[nx][ny] != z:
                ans = min(ans, dist[x][y])
                return
            #if a[nx][ny]==0, 바다 and dist[nx][ny]==-1:
            if not a[nx][ny] and dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] +1
                q.append((nx, ny))

#dfs를 돌려서 각 섬마다 번호를 붙이는 과정
for i in range(n):
    for j in range(n):
        if not check[i][j] and a[i][j]:
            dfs(i, j)
            k +=1

#각 번호붙여진 섬들에 대하여 bfs 돌리는 것
for i in range(1, k+1):
    bfs(i)

print(ans)