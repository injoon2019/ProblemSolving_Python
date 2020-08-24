'''
Problem Solving Baekjoon 2667_3
Author: Injun Son
Date: August 24, 2020
'''
import sys, copy
from collections import deque
sys.setrecursionlimit(100000)
dx = [-1, 0 ,0, 1]
dy = [0, 1, -1, 0]

N = int(input())
graph = [list(map(int, input())) for _ in range(N)]
count = 1
visit_check = [[0]*N for _ in range(N)]

def dfs(i, j):
    visit_check[i][j]=1
    graph[i][j]=count
    house_count[count]+=1
    for k in range(4):
        ny, nx = i+dy[k], j+dx[k]
        if 0<=nx<N and 0<=ny<N:
            if visit_check[ny][nx]==0 and graph[ny][nx]==1:
                dfs(ny, nx)

house_count = [0]*(N*N+1)
for i in range(N):
    for j in range(N):
        if visit_check[i][j]==0 and graph[i][j]==1:
            dfs(i, j)
            count +=1

print(count -1)
# for i in range(N):
#     for j in range(N):
#         print(graph[i][j], end= " ")
#     print("")
house_count.sort()
for i in range(1, len(house_count)):
    if house_count[i] != 0:
        print(house_count[i])

