'''
Problem Solving Baekjoon 4963
Author: Injun Son
Date: July 29, 2020
'''
import sys
from collections import deque
sys.setrecursionlimit(100000)
dx = [-1,-1,-1,  0, 0, 1, 1, 1]
dy = [1, 0, -1, 1, -1, 1, 0, -1]

def dfs(y, x):
    global arr
    arr[y][x]='0'
    for k in range(8):
        ny = y+dy[k]
        nx = x+dx[k]
        if ny>=0 and ny<h and nx>=0 and nx<w:
            if arr[ny][nx]=='1':
                dfs(ny, nx)

w, h = map(int, sys.stdin.readline().rstrip().split())
while not (w==0 and h==0):
    arr = [list(input().split()) for _ in range(h)]
    count = 0
    for i in range(h):
        for j in range(w):
            if arr[i][j]=='1':
                count +=1
                dfs(i, j)
    print(count)

    w, h = map(int, sys.stdin.readline().rstrip().split())