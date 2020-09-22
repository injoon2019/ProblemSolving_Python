'''
Problem Solving Baekjoon 17142
Author: Injun Son
Date: September 21, 2020
'''
import sys
import copy
from itertools import combinations
from collections import deque

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
virus_pos = []
empty_cells_count = 0

dx = [-1, 0, 0, 1]
dy = [0, 1, -1, 0]

def print_board(board):
    for i in  range(N):
        for j in range(N):
            print(board[i][j], end=" ")
        print()
    print()

for i in range(N):
    for j in range(N):
        if graph[i][j]==2:
            virus_pos.append([i,j])
        if graph[i][j]==0 :
            empty_cells_count += 1

min_ans = sys.maxsize

def bfs(virus_positions):
    global min_ans
    q = deque()

    dist = [[-1]*N for _ in range(N)]
    infected = 0
    local_maximum = -sys.maxsize
    for virus in virus_positions:
        dist[virus[0]][virus[1]] = 0
        q.append(virus)

    for virus_pos_cell in virus_pos:
        dist[virus_pos_cell[0]][virus_pos_cell[1]] = 0

    # print_board(dist)
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if nx<0 or nx>=N or ny<0 or ny>=N:
                continue
            #벽이 아니고,
            if (dist[ny][nx]==-1 and graph[ny][nx]!=1) or (dist[ny][nx] > dist[y][x]+1) or (dist[ny][nx]==0 and [ny,nx] not in virus_positions):
                dist[ny][nx] = dist[y][x]+1
                if dist[ny][nx]> local_maximum:
                    local_maximum = dist[ny][nx]

                q.append([ny, nx])
                #바이러스를 놓을 수 있는 공간이 아닌 순수하게 빈칸인 공간만 센다
                if graph[ny][nx] !=2:
                    infected +=1

                if infected == empty_cells_count:
                    min_ans = min(min_ans, local_maximum)

for poss_pos in list(combinations(virus_pos, M)):
    bfs(poss_pos)

if empty_cells_count ==0:
    print(0)
    exit()

if min_ans==sys.maxsize:
        print(-1)
else:
    print(min_ans)