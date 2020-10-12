'''
Problem Solving Baekjoon 17135
Author: Injun Son
Date: October 12 , 2020
'''
from collections import deque
import sys
from itertools import combinations
import copy

dy = [0, 1, -1, 0]
dx = [-1, 0, 0, 1]

N, M, D = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

possible_combs = list(combinations([i for i in range(M)], 3))
max_enemy = -sys.maxsize

def print_board(board):
    for i in range(N+1):
        for j in range(M):
            print(board[i][j], end=" ")
        print()
    print()

def BFS(archer, graph_copy):
    y, x = (N, archer)
    q = deque()
    q.append([y,x, 0])
    visit_check = [ [0]*M for _ in range(N+1)]
    visit_check[y][x] = 1
    while q:
        y, x, dist = q.popleft()
        if graph_copy[y][x]==1 and dist <= D:
            return [y, x]
        else:
            for i in range(4):
                ny, nx = y+dy[i], x+dx[i]
                if ny<0 or ny>=N+1 or nx<0 or nx>=M or visit_check[ny][nx]==1:
                    continue
                else:
                    visit_check[ny][nx] = 1
                    q.append([ny, nx, dist+1])

    return None


def Attack(archers, graph_copy):
    enemy_list = []
    for archer in archers:
        enemy_pos = BFS(archer, graph_copy)
        if enemy_pos not in enemy_list and enemy_pos != None:
            enemy_list.append(enemy_pos)

    for pos in enemy_list:
        if pos != None:
            graph_copy[pos[0]][pos[1]] = 0

    return len(enemy_list), graph_copy

def Move(graph_copy):
    graph_copy = graph_copy[:-2]
    graph_copy.append([2]*M)
    graph_copy = [[0]*M] + graph_copy
    return graph_copy

for comb in possible_combs:
    graph_copy = copy.deepcopy(graph)
    graph_copy.append([2]*M)
    local_max_enemy = 0
    # 열의 수만큼 반복한다
    for _ in range(N):
        killed_enemy, graph_copy = Attack(comb, graph_copy)
        local_max_enemy += killed_enemy
        graph_copy = Move(graph_copy)

    max_enemy = max(local_max_enemy, max_enemy)

print(max_enemy)