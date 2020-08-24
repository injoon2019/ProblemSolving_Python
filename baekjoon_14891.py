'''
Problem Solving Baekjoon 14891
Author: Injun Son
Date: August 23, 2020
'''
from collections import deque
import sys, copy
from itertools import combinations
gear_arr = [[]]
gear_arr+=   [deque(list(map(int, input())))  for _ in range(4)]
def print_gear():
    for i in gear_arr:
        print(i)
    print()

def rotate(gear_num, rotate_dir, right_left):
    #3시 방향, 9시 방향
    if right_left >0:
        if gear_num+1<=4:
            if gear_arr[gear_num+1][6] != gear_arr[gear_num][2]:
                rotate(gear_num+1, -rotate_dir, right_left)
    else:
        if gear_num-1 >=1:
            if gear_arr[gear_num-1][2] != gear_arr[gear_num][6]:
                rotate(gear_num-1, -rotate_dir, right_left)

    gear_arr[gear_num].rotate(rotate_dir)

def count_score():
    sum = 0
    #N극은0 S극은 1
    for i in range(1, len(gear_arr)):
        if gear_arr[i][0]==1:
            sum += 2**(i-1)
    return sum

k = int(input())
for _ in range(k):
    #1==clock wise, 2 == counterclockwise
    gear_num , dir = map(int, input().split())
    right = 9
    left = -9
    deque_backup = copy.deepcopy(gear_arr[gear_num])
    rotate(gear_num, dir, right)
    if gear_num != 1:
        gear_arr[gear_num] = deque_backup
        rotate(gear_num, dir, left)

score = count_score()
print(score)