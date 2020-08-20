'''
Problem Solving Baekjoon 2186
Author: Injun Son
Date: August 19, 2020
'''
from collections import deque
import sys, copy
from itertools import permutations
dx = [-1, 0, 0, 1]
dy = [0, 1, -1, 0]

def bfs(y, x):
    global ans
    q = deque()
    q.append([y, x, 0])
    while q:
        cur_pos = q.popleft()
        y = cur_pos[0]
        x = cur_pos[1]
        cur_index = cur_pos[2]

        for i in range(4):
            for k in range(1, m+1):
                ny = y + (dy[i] * k)
                nx = x + (dx[i] * k)
                if 0<=nx<c and 0<=ny<r and graph[ny][nx]==target[cur_index+1]:
                    if cur_index+1 == len(target) - 1:
                        ans+=1
                        continue
                    q.append([ny, nx, cur_index+1])

r, c, m = map(int, input().split())
graph = [list(input()) for _ in range(r)]
target=  input()
ans = 0
for i in range(r):
    for j in range(c):
        if graph[i][j]==target[0]:
            bfs(i,j)

print(ans)

'''
메모리 초과났다!
'''