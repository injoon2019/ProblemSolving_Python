'''
Problem Solving Baekjoon 2178
Author: Injun Son
Date: July 31, 2020
'''
import sys
from collections import deque
r, c = map(int, input().split())
dx = [-1, 0, 0, 1]
dy = [0, 1, -1, 0]

arr = [list(map(int, input())) for i in range(r)]
q = deque()
def bfs():
    q.append([0,0])
    while q:
        now = q.popleft()
        # print(now)
        for k in range(4):
            ny, nx = now[0]+ dy[k], now[1]+dx[k]
            if 0<=ny<r and 0<=nx<c and arr[ny][nx]>=1:
                if arr[ny][nx]==1:
                    arr[ny][nx] = arr[now[0]][now[1]]+1
                    q.append([ny, nx])

                elif arr[ny][nx] >1:
                    if arr[now[0]][now[1]]+1 < arr[ny][nx]:
                        arr[ny][nx] = arr[now[0]][now[1]]+1
                        q.append([ny, nx])
bfs()
print(arr[r-1][c-1])