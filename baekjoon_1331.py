'''
Problem Solving Baekjoon 1331
Author: Injun Son
Date: October 25, 2020
'''
import sys
import datetime

cur_pos = None
next_pos = None
first_pos = None
dx = [1, 2, 2, 1, -1, -2, -2, -1]
dy = [2, 1, -1, -2, -2, -1, 1, 2]

visited = [[0]*6 for _ in range(6)]

def check_inBoard(pos):
    return 0<=pos[0]<6 and 0<=pos[1]<6

def convert_pos(command):
    y = 6 - int(command[1])
    x = ord(command[0]) - ord('A')
    return [y, x]

def check_nightMove(cur_pos, next_pos):
    for i in range(8):
        ny, nx = cur_pos[0]+dy[i], cur_pos[1]+dx[i]
        if ny == next_pos[0] and nx == next_pos[1]:
            return True
    return False

def get_sum():
    temp = 0
    for i in range(6):
        temp += sum(visited[i])
    return temp

def check_last(cur_pos):
    # print(get_sum())
    return get_sum() == 36 and check_nightMove(cur_pos, first_pos)

def print_board():
    for i in range(6):
        for j in range(6):
            print(visited[i][j], end=" ")
        print()
    print()

for k in range(36):
    command = input()
    # print(command)
    if cur_pos == None:
        cur_pos = convert_pos(command)
        first_pos = cur_pos
        visited[cur_pos[0]][cur_pos[1]] = 1
        if not check_inBoard(cur_pos):
            print("Invalid")
            break

    else:
        visited[cur_pos[0]][cur_pos[1]] = 1
        next_pos = convert_pos(command)
        if check_inBoard(next_pos) and check_nightMove(cur_pos, next_pos) and visited[next_pos[0]][next_pos[1]]==0:
            cur_pos = next_pos
        else:
            # print(cur_pos, next_pos)
            print("Invalid")
            break

    if k==35:
        visited[cur_pos[0]][cur_pos[1]] = 1
        if not check_last(cur_pos):
            # print_board()
            print("Invalid")
            break
else:
    print("Valid")

