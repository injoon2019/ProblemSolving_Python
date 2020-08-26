'''
Problem Solving Baekjoon 1018
Author: Injun Son
Date: August 25, 2020
'''
import sys
from collections import deque
from itertools import combinations
from itertools import permutations
import math
sys.setrecursionlimit(100000)

r, c = map(int, input().split())
graph = [list(input()) for _ in range(r)]
min_num = sys.maxsize

def get_count(y, x):
    idx1= 0   # W로 시작했을 때 칠해야 할 부분
    idx2 = 0  # B로 시작했을 때 칠해야 할 부분
    for i in range(y, y+8):
        for j in range(x, x+8):
            if (i+j)%2==0:
                if graph[i][j]!='W': idx1 +=1
                if graph[i][j]!="B": idx2 +=1
            else:
                if graph[i][j] != 'B': idx1 += 1
                if graph[i][j] != "W": idx2 += 1
    return min(idx1, idx2)

for i in range(r-8+1):
    for j in range(c-8+1):
        count = get_count(i, j)
        min_num = min(min_num, count)

print(min_num)