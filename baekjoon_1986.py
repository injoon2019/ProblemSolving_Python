'''
Problem Solving Baekjoon 1986
Author: Injun Son
Date: November 1, 2020
'''
from collections import deque
import heapq
import sys

r, c = map(int, input().split())
graph = [[0]*c for _ in range(r)]
queens_list = []
knights_list = []
pawns_list = []

qdx = [0, 1, 1, 1, 0, -1, -1, -1]
qdy = [-1, -1, 0, 1, 1, 1, 0, -1]

kdx = [1, 2, 2, 1, -1, -2, -2, -1]
kdy = [-2, -1, 1, 2, 2, 1, -1, -2]

queen_input = list(map(int, input().split()))
y, x = 1, 2
for i in range(queen_input[0]):
    qy = queen_input[y]-1
    qx = queen_input[x]-1
    queens_list.append([qy, qx])
    y, x = y+2, x+2

knight_input = list(map(int, input().split()))
y, x = 1, 2
for i in range(knight_input[0]):
    ky = knight_input[y]-1
    kx = knight_input[x]-1
    knights_list.append([ky, kx])
    y, x = y+2, x+2

pawn_input = list(map(int, input().split()))
y, x = 1, 2
for i in range(pawn_input[0]):
    ky = pawn_input[y]-1
    kx = pawn_input[x]-1
    pawns_list.append([ky, kx])
    y, x = y+2, x+2

def print_board():
    for i in range(r):
        for j in range(c):
            print(graph[i][j], end=" ")
        print()
    print()

def queen_move(y, x):
    for i in range(8):
        for q in range(1, max(r, c)):
            ny, nx = y+ qdy[i]*q , x+ qdx[i]*q
            if 0<=ny<r and 0<=nx<c and graph[ny][nx] not in [1,2,3]:
                graph[ny][nx] = 4
            else:
                break

def knight_move(y, x):
    for i in range(8):
        ny, nx = y+kdy[i], x+kdx[i]
        if 0<=ny<r and 0<=nx<c and graph[ny][nx] not in [1,2,3]:
            graph[ny][nx] = 6

for pawn in pawns_list:
    graph[pawn[0]][pawn[1]] = 1

for knight in knights_list:
    graph[knight[0]][knight[1]] = 2

for queen in queens_list:
    graph[queen[0]][queen[1]] = 3

for queen in queens_list:
    queen_move(queen[0], queen[1])

for knight in knights_list:
    knight_move(knight[0], knight[1])

ans = 0
for i in range(r):
    for j in range(c):
        if graph[i][j]==0:
            ans +=1

print(ans)
# print_board()