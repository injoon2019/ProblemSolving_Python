'''
Problem Solving Baekjoon 2580
Author: Injun Son
Date: August 19, 2020
'''
from collections import deque
import sys, copy
from itertools import permutations

board = [list(map(int, input().split())) for _ in range(9)]
coordinates = []
def print_board(board):
    for i in range(9):
        for j in range(9):
            print(board[i][j], end=" ")
        print()

def i_not_in_row(k,y,x, board):
    if k in board[y]:
        return False
    return True

def i_not_in_column(k, y, x, board):
    for i in range(9):
        if board[i][x]==k:
            return False
    return True

def i_not_in_square(k, y, x, board):
    s_y, s_x = y//3, x//3
    for i in range(3):
        for j in range(3):
            if board[s_y*3 +i][s_x*3 +j]==k:
                return False
    return True

def back_tracking(board, coordinates, index):

    if index==len(coordinates):
        print_board(board)
        exit()

    else:
        y, x = coordinates[index]
        back_up = board[y][x]
        for i in range(1, 10):
            if i_not_in_row(i, y, x, board) and i_not_in_column(i, y, x, board) and i_not_in_square(i,y,x, board):
                board[y][x] = i
                back_tracking(board, coordinates, index+1)
                board[y][x] = back_up

#0인 곳들 조사
for i in range(9):
    for j in range(9):
        if board[i][j]==0:
            coordinates.append([i, j])

back_tracking(board, coordinates, 0)

'''
마지막에 도달하고 출력하고나면 return이 아닌 exit을 해야한다. 그렇지 않으면 또 돌아가서 backtracking을 계속 할 것이다. 
'''