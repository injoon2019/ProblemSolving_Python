'''
Problem Solving Baekjoon 7562
Author: Injun Son
Date: September 22, 2020
'''
import sys
import copy
from itertools import combinations
from collections import deque

dx = [1, 2, 2, 1, -1, -2, -2, -1]
dy = [2, 1, -1, -2, -2, -1, 1, 2]

def bfs(y, x, ty, tx):
    q = deque()
    check = dict()
    check[(y,x)] = 1
    q.append((y,x, 0))
    while q:
        y, x, cnt = q.popleft()
        if (y, x) == (ty, tx):
            return cnt
        else:
            for i in range(len(dx)):
                ny, nx = y+dy[i], x+dx[i]
                if ny<0 or ny>=N or nx<0 or nx>=N or (ny, nx) in check:
                    continue
                else:
                    check[(ny, nx)] = 1
                    q.append((ny, nx, cnt+1))

T = int(input())
for _ in range(T):
    N = int(input())
    cur_y, cur_x = map(int, input().split())
    tar_y, tar_x = map(int, input().split())
    # graph = [[0]*N for _ in range(N)]
    print(bfs(cur_y, cur_x, tar_y, tar_x))