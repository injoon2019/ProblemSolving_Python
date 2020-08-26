'''
Problem Solving Baekjoon 2146_2
Author: Injun Son
Date: Aug 26, 2020
'''
import sys
sys.setrecursionlimit(10**6)
from collections import deque

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
check = [[False]*N for _ in range(N)]
'''
dfs로 각 섬에 1번부터 번호를 붙여준다
'''
dx = [-1, 0 ,0, 1]
dy = [0, 1, -1, 0]
ans = sys.maxsize
count = 1
#각 섬에 번호를 붙여줘서 구분하기 위함이다
def dfs(y, x):
    global count
    check[y][x] = True
    graph[y][x] = count
    for i in range(4):
        ny, nx = y+dy[i], x+dx[i]
        if ny<0 or ny>=N or nx<0 or nx>=N:
            continue
        if check[ny][nx]==False and graph[ny][nx]:
            dfs(ny, nx)

def bfs(z):
    global ans
    dist = [[-1]*N for _ in range(N)]
    q = deque()
    for i in range(N):
        for j in range(N):
            if graph[i][j]==z:
                q.append([i, j])
                dist[i][j]=0

    while q:
        y, x = q.popleft()
        for i in range(4):
            ny, nx = y +dy[i], x+dx[i]
            if ny<0 or ny>=N or nx<0 or nx>=N:
                continue
            #다른 섬에 도착을 한 경우이다
            if graph[ny][nx]>0 and graph[ny][nx] !=z:
                ans = min(ans, dist[y][x])
                return
            # 만약 바다이고, 간척사업도 안된 곳이라면 새로 거리를 더해준다
            if graph[ny][nx]==0 and dist[ny][nx]==-1:
                dist[ny][nx] = dist[y][x] +1
                q.append([ny, nx])

    print_board(dist)
    print()


for i in range(N):
    for j in range(N):
        if check[i][j]==False and graph[i][j]==1:
            dfs(i, j)
            count +=1

def print_board(board):
    for i in range(N):
        for j in range(N):
            print(board[i][j], end=" ")
        print("")


# 각각의 섬에 대하여 bfs로 간척을 하듯이 다른 섬에 도달한다
for i in range(1, count):
    bfs(i)

print(ans)