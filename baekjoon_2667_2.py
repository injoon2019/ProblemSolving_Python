'''
Problem Solving Baekjoon 2667_2
Author: Injun Son
Date: July 29, 2020
'''
import sys
from collections import deque
sys.setrecursionlimit(100000)
dx = [-1, 0 ,0, 1]
dy = [0, 1, -1, 0]

N = int(sys.stdin.readline())
arr = [list(input()) for _ in range(N)]
count_list = []

def dfs(y, x):
    global arr, count
    arr[y][x]='0'
    count +=1
    for k in range(4):
        ny, nx = y+dy[k], x+dx[k]
        if ny>=0 and ny<N and nx>=0 and nx<N:
            if arr[ny][nx]=='1':
                dfs(ny, nx)


for i in range(N):
    for j in range(N):
        if arr[i][j]=='1':
            count = 0
            dfs(i, j)
            count_list.append(count)

count_list.sort()
print(len(count_list))
for i in count_list:
    print(i)
