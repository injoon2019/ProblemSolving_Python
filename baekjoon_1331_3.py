'''
Problem Solving Baekjoon 1331_2
Author: Injun Son
Date: October 25, 2020
'''
import sys
import datetime

command_list = [input() for _ in range(36) ]
command_list += [command_list[0]]
visited = set()
valid = True
for i in range(36):
    cur_pos = ( ord(command_list[i][0]) - ord('A'), int(command_list[i][1]))
    next_pos = ( ord(command_list[i+1][0]) - ord('A'), int(command_list[i+1][1]))
    dir = ( abs(cur_pos[0]-next_pos[0]), abs(cur_pos[1]-next_pos[1]))
    if dir == (1, 2) or dir == (2, 1):
        visited.add(cur_pos)
        continue
    valid = False
    break
if not valid or len(visited) != 36: print("Invalid")
else: print("Valid")