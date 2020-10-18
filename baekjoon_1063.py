'''
Problem Solving Baekjoon 1063
Author: Injun Son
Date: October 17, 2020
'''

from collections import deque
import sys

graph = [ [0]*8 for _ in range(8)]

alpha_dict = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7}
arr_dict = dict((value, key) for key, value in alpha_dict.items())
king, rock, N = input().split()
king_pos = [8-int(king[1]), alpha_dict[king[0]]]
rock_pos = [8-int(rock[1]), alpha_dict[rock[0]]]


def rock_exist(command, horse):
    tmp_horse = move(command, king_pos)
    return tmp_horse == rock_pos

def arr2chess(pos):
    print(arr_dict[pos[1]]+str(8-pos[0]))

def move(command, horse):
    if command=='R':
        return [horse[0] ,horse[1] + 1]
    elif command =='L':
        return [horse[0], horse[1] - 1]
    elif command =='B':
        return [horse[0]+1, horse[1]]
    elif command =='T':
        return [horse[0]-1, horse[1] ]
    elif command =='RT':
        return [horse[0]-1, horse[1]+ 1]
    elif command =='LT':
        return [horse[0]-1, horse[1] - 1]
    elif command =='RB':
        return [horse[0]+1, horse[1] + 1]
    elif command =='LB':
        return [horse[0]+1, horse[1] - 1]

def out_bound(command, horse):
    tmp_horse = move(command, horse)
    return not (0<=tmp_horse[0]<8 and 0<=tmp_horse[1]<8)

for i in range(int(N)):
    move_command = input()
    if rock_exist(move_command, king):
        if out_bound(move_command, rock_pos) or out_bound(move_command, king_pos):
            continue
        else:
            rock_pos = move(move_command, rock_pos)
            king_pos = move(move_command, king_pos)
    else:
        if out_bound(move_command, king_pos):
            continue
        else:
            king_pos = move(move_command, king_pos)

arr2chess(king_pos)
arr2chess(rock_pos)