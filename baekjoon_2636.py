'''
Problem Solving Baekjoon 2636
Author: Injun Son
Date: October 27, 2020
'''
import sys
import math
from collections import deque
'''
1. 치즈에서 bfs를 이용해서 가장 자리를 알아내려 했으나, 내부에 있는 구멍 때문에 감이 안왔다.
2. 역으로 외부 공기와 내부 공기를 구분해서 할 수 있다. (0,0)은 항상 외부이므로, 여기에서 bfs 사용하면된다.  
(bfs를 돌릴때 치즈면 공기로 바꾸고 큐에는 추가하지 않는다. 방문하지 않은 공기면 큐에 추가한다)
'''

dx = [-1, 0, 0, 1]
dy = [0, 1, -1, 0]

r, c  = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(r)]

def print_board():
    for i in range(r):
        for j in range(c):
            print(graph[i][j], end=" ")
        print()
    print()

def cheese_count():
    cheese_left = 0
    for i in range(r):
        for j in range(c):
            if graph[i][j]==1:
                cheese_left +=1
    return cheese_left

def bfs_first():
    global visited
    queue = deque()
    queue.append([0,0])
    visited = [[0] * c for _ in range(r)]
    visited[0][0] = 1
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if 0<=nx<c and 0<=ny<r and visited[ny][nx]==0 and graph[ny][nx]==0:
                visited[ny][nx] = 1

def bfs():
    global visited
    queue = deque()
    queue.append([0,0])
    visited = [[0] * c for _ in range(r)]
    visited[0][0] = 1
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if 0<=nx<c and 0<=ny<r:
                # 외부 치즈인 경우
                if visited[ny][nx]==0 and graph[ny][nx]==1:
                    visited[ny][nx] = 1
                    graph[ny][nx] = 0
                # 내부, 외부 공기인 경우
                if visited[ny][nx]==0 and graph[ny][nx]==0:
                    visited[ny][nx] = 1
                    queue.append([ny, nx])

# print_board()
bfs_first()
ans_count = 0
last_left = 0
while cheese_count():
    last_left = cheese_count()
    bfs()
    ans_count +=1

print(ans_count)
print(last_left)