'''
Problem Solving Baekjoon 1012
Author: Injun Son
Date: August 24, 2020
'''
import sys
from collections import deque
from itertools import combinations
from itertools import permutations
import math
sys.setrecursionlimit(100000)

T = int(input())
dx = [-1, 0, 0, 1]
dy = [0, 1, -1, 0]

def bfs(y, x):
    visit_check = [[0] * c for _ in range(r)]
    q = deque()
    q.append([y, x])
    visit_check[y][x] = 1
    while q:
        pos_list = q.popleft()
        y_pos, x_pos = pos_list[0], pos_list[1]
        visit_check[y][x] = 1
        for i in range(4):
            ny , nx = y_pos+dy[i], x_pos+dx[i]
            if 0<=nx<c and 0<=ny<r and visit_check[ny][nx]==0 and graph[ny][nx]==1:
                visit_check[ny][nx]=1
                graph[ny][nx]=0
                q.append([ny, nx])

for _ in range(T):
    c, r, k = map(int, input().split())
    graph = [[0]*c for _ in range(r)]
    for _ in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1

    count = 0
    for i in range(r):
        for j in range(c):
            if graph[i][j]==1:
                bfs(i, j)
                count +=1
    print(count)