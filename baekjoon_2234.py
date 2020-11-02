'''
Problem Solving Baekjoon 2234
Author: Injun Son
Date: November 2, 2020
'''
import sys
from collections import deque
from itertools import combinations
# 서쪽에 벽이 있을 때는 1을, 북쪽에 벽이 있을 때는 2를,
# 동쪽에 벽이 있을 때는 4를, 남쪽에 벽이 있을 때는 8을 더한 값이 주어진다.

#서, 북, 남, 동
# 0, 1, 2,  3
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

c, r = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(r)]
visited = [[0]*c for _ in range(r)]

room_num = 1
max_roomSize = 0

def print_board(board):
    for i in range(r):
        for j in range(c):
            print(board[i][j], end=" ")
        print()

def movable(y, x):
    #서 북 남 동에서 하나씩 뺀다
    move_list = [0, 1, 2, 3]
    if graph[y][x]==0:
        return move_list

    #서
    if graph[y][x] & 1:
        move_list.remove(0)
    #북
    if graph[y][x] & 2:
        move_list.remove(1)
    #남
    if graph[y][x] & 8:
        move_list.remove(2)
    #동
    if graph[y][x] & 4:
        move_list.remove(3)

    return move_list

def adjacent(v1, v2):
    for i in range(r):
        for j in range(c):
            y, x = i, j
            for k in range(4):
                ny, nx = y+dy[k], x+dx[k]
                if 0<=ny<r and 0<=nx<c and visited[y][x]==v1 and visited[ny][nx]==v2:
                    return True
    return False

def bfs(y, x):
    queue = deque()
    queue.append([y, x])
    visited[y][x] = room_num
    while queue:
        y, x = queue.popleft()
        for i in movable(y,x):
            ny, nx = y+dy[i], x+dx[i]
            if 0<=ny<r and 0<=nx<c and visited[ny][nx]==0:
                visited[ny][nx] = room_num
                queue.append([ny, nx])

for i in range(r):
    for j in range(c):
        if visited[i][j]==0:
            bfs(i, j)
            room_num +=1

roomSize_list = [0]*(room_num)
for i in range(r):
    for j in range(c):
        roomSize_list[visited[i][j]] +=1

# print_board(visited)
possible_combs = list(combinations([i for i in range(1, room_num)], 2))
for comb in possible_combs:
    if roomSize_list[comb[0]]+ roomSize_list[comb[1]] > max_roomSize:
        if adjacent(comb[0], comb[1]):
            max_roomSize = roomSize_list[comb[0]]+ roomSize_list[comb[1]]

print(room_num-1)
print(max(roomSize_list))
print(max_roomSize)