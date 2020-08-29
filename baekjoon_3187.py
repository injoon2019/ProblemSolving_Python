'''
Problem Solving Baekjoon 3187
Author: Injun Son
Date: August 29, 2020
'''
import sys
from collections import deque

dx = [-1, 0, 0, 1]
dy = [0, 1, -1, 0]

r, c = map(int, input().split())
graph = [list(input()) for _ in range(r)]
check_visited = [[0]*c for _ in range(r)]

def print_board(board):
    global r, c
    for i in range(r):
        for j in range(c):
            print(board[i][j], end="")
        print()

# print_board(graph)
#그룹화 먼저 해주자
group_num =1
groups = dict()
def bfs(y, x):
    check_visited[y][x]=1
    q =  deque()
    q.append([y, x])
    groups[group_num] = [0, 0]
    if graph[y][x] == 'v':
        # 해당 그룹의 늑대, 양
        groups[group_num][0] += 1
    elif graph[y][x] == 'k':
        # 해당 그룹의 늑대, 양
        groups[group_num][1] += 1

    while q:
        y, x = q.popleft()
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if 0<=ny<r and 0<=nx<c:
                if not check_visited[ny][nx] and graph[ny][nx]!="#":
                    #갯수 더해주기
                    if graph[ny][nx] == 'v':
                        # 해당 그룹의 늑대, 양
                        groups[group_num][0]+=1
                    elif graph[ny][nx] == 'k':
                        # 해당 그룹의 늑대, 양
                        groups[group_num][1]+= 1
                    check_visited[ny][nx] = 1
                    q.append([ny, nx])

for i in range(r):
    for j in range(c):
        if not check_visited[i][j] and graph[i][j] != '#':
            bfs(i, j)
            group_num +=1

wolves, sheeps = 0, 0
for _, group in enumerate(groups):
    wolf = groups[group][0]
    sheep = groups[group][1]
    if sheep> wolf:
        wolf = 0
    else:
        sheep = 0
    wolves += wolf
    sheeps += sheep
print(sheeps, wolves)