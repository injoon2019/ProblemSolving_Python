'''
Problem Solving Baekjoon 3055
Author: Injun Son
Date: September 11, 2020
'''
import sys
from heapq import heappop, heappush
import copy
from collections import deque

r, c  = map(int, input().split())
graph = [list(input()) for _ in range(r)]

dx = [-1,0,0,1]
dy = [0,1,-1,0]

dod_pos = [0,0]
water_pos = deque()

def spread_water():
    tmp = copy.deepcopy(water_pos)
    for water in tmp:
        y, x = water
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if 0<=nx<c and 0<=ny<r and graph[ny][nx]!='*' and graph[ny][nx]!='D' and graph[ny][nx]!='X':
                graph[ny][nx]='*'
                water_pos.append([ny, nx])

for i in range(r):
    for j in range(c):
        if graph[i][j] =='S':
            dod_pos = [i,j]
        elif graph[i][j]=='*':
            water_pos.append([i,j])

def bfs(y, x):
    q = deque()
    q.append([y, x, 0])
    visited = dict()
    visited[(y,x)] = 1
    while q:
        q_len = len(q)
        for j in range(q_len):
            y, x, time = q.popleft()
            if graph[y][x] == 'D':
                print(time)
                return
            if graph[y][x] == '*':
                continue

            for i in range(4):
                ny, nx = y+dy[i], x+dx[i]
                if 0<=nx<c and 0<=ny<r and graph[ny][nx]!='*' and graph[ny][nx]!='X' and ( (ny,nx) not in visited.keys() or visited[(ny, nx)]==0):
                    visited[(ny, nx)] = 1
                    if graph[ny][nx]=='D':
                        print(time+1)
                        return
                    graph[ny][nx]='S'
                    q.append([ny, nx, time+1])

        spread_water()
    print("KAKTUS")

bfs(dod_pos[0], dod_pos[1])

'''
푼 방법: 일단 고슴 도치 이동 bfs 돌린다. 이때 일반적인  돌리기가 아니라 물과 고슴도치의 이동 속도를 맞추려면
q에 있는 모든 고슴도치의 position에서 돌려야 이동 1번 한 것이다.
그리고 나서 물은 이동을 하며 고슴도치가 있는 곳이면 물로 덮어버린다. 
'''



