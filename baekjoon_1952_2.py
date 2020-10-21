'''
Problem Solving Baekjoon 1952
Author: Injun Son
Date: October 21, 2020
'''
import math, sys

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

r, c = map(int, input().split())
graph = [[0]*c for _ in range(r)]

count = 0
ans = 0
cur_y, cur_x =0, 0
dir = 0

while count < r*c:
    while 0<=cur_y<r and 0<=cur_x<c and graph[cur_y][cur_x]==0:
        # print(cur_y, cur_x)
        graph[cur_y][cur_x] = count+1
        count +=1
        cur_y, cur_x = cur_y+dy[dir], cur_x+dx[dir]
    # print(cur_y, cur_x)
    cur_y -= dy[dir]
    cur_x -= dx[dir]
    dir = (dir+1)%4
    cur_y += dy[dir]
    cur_x += dx[dir]
    ans +=1
#
# for i in range(r):
#     for j in range(c):
#         print(graph[i][j], end=" ")
#     print()

print(ans-1)



