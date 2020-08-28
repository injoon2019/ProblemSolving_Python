'''
Problem Solving Baekjoon 14499
Author: Injun Son
Date: August 28, 2020
'''
import math, sys, copy

r, c, y, x, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(r)]
dir_arr = list(map(int, input().split()))
dice = [[0]*3 for _ in range(4)]
'''
' 2 '
4 1 3
' 5 '
' 6 '
'''

def east():
    dice2 = copy.deepcopy(dice)
    dice[0][1] = dice2[0][1]
    dice[1][0] = dice2[1][1]
    dice[1][1] = dice2[1][2]
    dice[1][2] = dice2[3][1]
    dice[2][1] = dice2[2][1]
    dice[3][1] = dice2[1][0]
    print(dice[3][1])

def west():
    dice2 = copy.deepcopy(dice)
    dice[0][1] = dice2[0][1]
    dice[1][0] = dice2[3][1]
    dice[1][1] = dice2[1][0]
    dice[1][2] = dice2[1][1]
    dice[2][1] = dice2[2][1]
    dice[3][1] = dice2[1][2]
    print(dice[3][1])

def north():
    dice2 = copy.deepcopy(dice)
    dice[0][1] = dice2[3][1]
    dice[1][0] = dice2[1][0]
    dice[1][1] = dice2[0][1]
    dice[1][2] = dice2[1][2]
    dice[2][1] = dice2[1][1]
    dice[3][1] = dice2[2][1]
    print(dice[3][1])

def south():
    dice2 = copy.deepcopy(dice)
    dice[3][1] = dice2[0][1]
    dice[1][0] = dice2[1][0]
    dice[1][1] = dice2[2][1]
    dice[1][2] = dice2[1][2]
    dice[2][1] = dice2[3][1]
    dice[0][1] = dice2[1][1]
    print(dice[3][1])

def copy_dice_to_graph(y, x):
    graph[y][x] =  dice[1][1]

def copy_graph_to_dice(y, x):
    dice[1][1] = graph[y][x]

#동 서 북 남
#1 2 3 4
dx = [0, 1, -1, 0, 0]
dy = [0, 0, 0, -1, 1]
for i in dir_arr:
    ny = y+dy[i]
    nx = x+dx[i]
    # print(ny, nx)
    if 0<=ny<r and 0<=nx<c:
        if i==1:
            east()
        elif i==2:
            west()
        elif i==3:
            north()
        elif i==4:
            south()

        #주사위의 바닥면에 쓰여 있는 수가 칸에 복사된다
        if graph[ny][nx]==0:
            copy_dice_to_graph(ny, nx)
        else:
            copy_graph_to_dice(ny, nx)
            graph[ny][nx]=0

        y = ny
        x = nx