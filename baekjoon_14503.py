'''
Problem Solving Baekjoon 14503
Author: Injun Son
Date: August 25, 2020
'''
import sys, copy
from collections import deque


# 북동남서
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

# 방향 바꿔주기)
def change(d):
    if d==0:
        return 3
    elif d==1:
        return 0
    elif d==2:
        return 1
    elif d==3:
        return 2

def find(r, c, d):
    cnt = 1
    y = r
    x = c
    graph[y][x]=2
    while True:
        dc = d
        for i in range(4):
            empty = 0
            dc = change(dc)
            ny = y + dy[dc]
            nx = x + dx[dc]
            # 유효 범위 안에 있고, 빈칸이라면
            if (0<=nx<m and 0<=ny<n and graph[ny][nx]==0):
                cnt +=1
                x = nx
                y= ny
                graph[ny][nx] = 2
                d = dc
                empty = 1
                break
        #4방향 모두 탐색 후, 모든 칸이 청소가 되어 있다면
        if empty ==0:
            # 후진
            if d==0:
                y+=1
            elif d==1:
                x-=1
            elif d==2:
                y-=1
            elif d==3:
                x +=1
            # 후진하려는 칸이 벽이라면 stop
            if graph[y][x]==1:
                break
    return cnt


n, m = map(int, input().split())
r, c, d = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
ans = find(r, c, d)
print(ans)

