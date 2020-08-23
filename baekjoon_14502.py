'''
Problem Solving Baekjoon 14502
Author: Injun Son
Date: August 23, 2020
'''
from collections import deque
import sys, copy
from itertools import combinations
r, c = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(r)]
possible_coordinates= []
virus_positions = []

dx = [-1, 0, 0, 1]
dy = [0, 1, -1, 0]

def print_board(board):
    for i in range(r):
        for j in range(c):
            print(board[i][j], end=" ")
        print()

#0인 좌표들 조사
for i in range(r):
    for j in range(c):
        if graph[i][j]==0:
            possible_coordinates.append([i, j])
        elif graph[i][j]==2:
            virus_positions.append([i,j])

#0인 좌표들의 리스트 중에서 3개 combination 경우의 수 구하기
coordinates_comb = list(combinations(possible_coordinates, 3))

MAX_AREA = 0
ans_board=None

#벽을 세울 수 있는 모든 경우의 수
for comb in coordinates_comb:
    graph_copy = copy.deepcopy(graph)
    #벽 세우기 완료
    for coordinate in comb:
        graph_copy[coordinate[0]][coordinate[1]] = 1

    #바이러스 전파 시뮬레이션
    q = deque(virus_positions)
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0<=nx<c and 0<=ny<r and graph_copy[ny][nx]==0:
                graph_copy[ny][nx]=2
                q.append([ny, nx])
    #안전한 지역 넓이
    area = 0
    for i in range(r):
        for j in range(c):
            if graph_copy[i][j]==0:
                area +=1

    if area> MAX_AREA:
        ans_board = copy.deepcopy(graph_copy)
    MAX_AREA = max(MAX_AREA, area)

print(MAX_AREA)


