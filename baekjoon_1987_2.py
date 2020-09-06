'''
Problem Solving Baekjoon 1987_2
Author: Injun Son
Date: September 6, 2020
'''
from collections import deque
import sys
input = sys.stdin.readline
R, C = map(int, input().split())
graph = [list(input()) for _ in range(R)]
dx = (-1,0,0,1)
dy = (0,-1,1,0)

max_count = -1*sys.maxsize
check = [False]*26

def dfs(y, x, count):
    global max_count
    max_count = max(max_count, count)
    for i in range(4):
        ny, nx = y+dy[i], x+dx[i]
        if nx<0 or nx>=C or ny<0 or ny>=R:
            continue
        c = ord(graph[ny][nx])-ord('A')
        if not check[c]:
            check[c] = True
            dfs(ny, nx, count+1)
            check[c] = False

check[ord(graph[0][0])-ord('A')] = True
dfs(0,0, 1)
print(max_count)