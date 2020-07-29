'''
Problem Solving Baekjoon 2667
Author: Injun Son
Date: July 28, 2020
'''
import sys
from collections import deque
sys.setrecursionlimit(200000)
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]
cnt = 0

def dfs(y, x):
    global cnt
    arr[y][x] = '0' #방문한 곳은 0
    cnt +=1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx<0 or nx>=N or ny<0 or ny>=N:
            continue

        if arr[ny][nx]=='1':
            dfs(ny, nx)


N = int(input())
arr = [list(input()) for i in range(N)]
apt_count = []
for i in range(N):
    for j in range(N):
        if arr[i][j]=='1':
            cnt =0
            dfs(i, j)
            apt_count.append(cnt)

print(len(apt_count))
apt_count.sort()
for i in apt_count:
    print(i)




