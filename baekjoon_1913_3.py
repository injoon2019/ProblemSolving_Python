'''
Problem Solving Baekjoon 1913_3
Author: Injun Son
Date: October 22, 2020
'''
import math, sys, copy
# 아래 오른 위 왼
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

N = int(input())
K = int(input())
graph = [[0]*N for _ in range(N)]
count = N*N
cur_y, cur_x = 0, 0
dir = 0

def print_board():
    for i in range(N):
        for j in range(N):
            print(graph[i][j], end=" ")
        print()

while count > 0 :
    while 0<=cur_y<N and 0<=cur_x<N and graph[cur_y][cur_x] ==0:
        graph[cur_y][cur_x] = count
        count -= 1
        cur_y += dy[dir]
        cur_x += dx[dir]

    cur_y -= dy[dir]
    cur_x -= dx[dir]
    dir = (dir+1)%4
    cur_y += dy[dir]
    cur_x += dx[dir]

print_board()
for i in range(N):
    for j in range(N):
        if graph[i][j] == K:
            print(i+1, j+1)
            break



