'''
Problem Solving Baekjoon 1194
Author: Injun Son
Date: October 29, 2020
'''
from collections import deque
import sys
from itertools import combinations
input = sys.stdin.readline
dx = [-1, 0, 0, 1]
dy = [0, 1, -1, 0]

'''
a키만 갖고 있을 때 : 000001
b키만 갖고 있을 때 : 000010
a,b 둘다 있으면   : 000011
'''

def bfs():
    while q:
        y, x, c, cnt = q.popleft()
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if 0<=ny<n and 0<=nx<m and s[ny][nx] !='#' and visit[ny][nx][c]==0:
                if s[ny][nx]==".":
                    visit[ny][nx][c] =1
                    q.append([ny, nx, c, cnt+1])
                elif s[ny][nx]=="1":
                    return cnt+1
                else:
                    if s[ny][nx].isupper():
                        if c & 1 << (ord(s[ny][nx]) - ord('A')):
                            visit[ny][nx][c] = 1
                            q.append([ny, nx, c, cnt+1])
                    elif s[ny][nx].islower():
                        nc = c | (1 << ord(s[ny][nx]) - ord('a'))
                        if visit[ny][nx][nc] ==0:
                            visit[ny][nx][nc] = 1
                            q.append([ny, nx, nc, cnt+1])
    return -1

n, m = map(int, input().split())
s = []
q = deque()
visit = [[[0]*64 for _ in range(m)] for _ in range(n)]
for i in range(n):
    a = list(input().strip())
    s.append(a)
    for j in range(m):
        if a[j] == '0':
            q.append([i, j, 0, 0])
            s[i][j] = "."
            visit[i][j][0] = 1
print(bfs())