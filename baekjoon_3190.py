'''
Problem Solving Baekjoon 3190
Author: Injun Son
Date: September 6, 2020
'''
import math, sys
import copy
from collections import deque

def print_board():
    tmp_board = copy.deepcopy(graph)
    for snake_position in snake_positions:
        s_y, s_x =snake_position
        tmp_board[s_y][s_x] = 2

    print("TIME", TIME, "DIR", DIR)
    for i in range(N):
        for j in range(N):
            print(tmp_board[i][j], end=" ")
        print()
    print()

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

#보드의 크기
N = int(input())
#사과의 개수
K = int(input())
apples = [ list(map(int, input().split())) for _ in range(K)]
# L 방향 변환 횟수
L = int(input())
moves = []
for _ in range(L):
    sec, dir = input().split()
    moves.append([int(sec), dir])

TIME = 0
DIR = 0

graph = [[0]*N for _ in range(N)]
for i in range(K):
    graph[apples[i][0]-1][apples[i][1]-1] = 1

snake_positions = deque()
snake_positions.append([0,0])

while True:
    #이동할 계획의 시간대가 맞으면 DIR을 바꿔준다
    if len(moves)>0 and moves[0][0]==TIME:
        #왼쪽 방향으로 90도 회전
        if moves[0][1]=='L':
            if DIR>=1:
                DIR -=1
            elif DIR==0:
                DIR =3
        #오른쪽 방향으로 90도 회전
        else:
            DIR = (DIR+1)%4
        moves = moves[1:]

    head_position = snake_positions[-1]
    new_head_y = head_position[0]+ dy[DIR]
    new_head_x = head_position[1]+ dx[DIR]
    TIME +=1
    #벽에 부딛히거나 자기 몸에 닿으면 게임 끝
    if new_head_x<0 or new_head_x>=N or new_head_y<0 or new_head_y>=N or [new_head_y, new_head_x] in snake_positions:
        break

    #어디 부딪히지 않고 다음칸에 사과가 있었다면
    if graph[new_head_y][new_head_x]==1:
        graph[new_head_y][new_head_x]=0
        snake_positions.append([new_head_y, new_head_x])

    #다음 칸에 사과가 없다면
    else:
        snake_positions.popleft()
        snake_positions.append([new_head_y, new_head_x])



print(TIME)
