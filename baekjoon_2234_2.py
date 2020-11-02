'''
Problem Solving Baekjoon 2234_2
Author: Injun Son
Date: November 2, 2020
'''
import sys
from collections import deque
from itertools import combinations

input = sys.stdin.readline
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]
dir = [1, 2, 4, 8]

def bfs(y, x, cnt):
    q.append([y, x])
    c[y][x] = cnt
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0<=ny < m and 0<=nx<n:
                if dir[i] & ~a[ny][nx] and c[ny][nx]==0:
                    c[ny][nx] = cnt
                    q.append([ny, nx])

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(m)]
c = [[0]*n for _ in range(m)]
q = deque()

cnt = 1
for i in range(m):
    for j in range(n):
        if c[i][j] ==0:
            bfs(i, j, cnt)
            cnt +=1
print(cnt - 1)

ans = [0]*(cnt - 1)
for i in range(m):
    for j in range(n):
        ans[c[i][j]-1] +=1
print(max(ans))

max_room = 0
for i in range(m):
    for j in range(n):
        for k in range(4):
            ni = i + dx[k]
            nj = j + dy[k]
            if 0<= ni < m and 0<= nj <n:
                if c[i][j] != c[ni][nj]:
                    room = ans[c[i][j]-1] + ans[c[ni][nj]-1]
                    max_room = max(room, max_room)
print(max_room)