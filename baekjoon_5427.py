'''
Problem Solving Baekjoon 5427
Author: Injun Son
Date: August 29, 2020
'''
import sys
from collections import deque
T = int(input())

dx = [-1, 0, 0, 1]
dy = [0, 1, -1, 0]

def bfs_fire():
    y, x = fire_q.popleft()
    added_fire_q =
    while fire_q:
        ny, nx = y+dy[i], x+dx[i]
        if 0<=nx<c and 0<=ny<r and graph[ny][]
for _ in range(T):
    c, r = map(int, input().split())
    graph = [list(input()) for _ in range(r)]

    #상근이의 위치와 불 조사
    person = [0,0]
    fire_q = deque()
    added_fire_q = deque()
    for i in range(r):
        for j in range(c):
            if graph[i][j] == '@':
                person = [i, j]
            elif graph[i][j] == '*':
                deque.append([i, j])
    
    #불이 먼저 옮겨붙고, 상근이가 이동하는 걸로 시뮬레이션 하자
    bfs_fire()