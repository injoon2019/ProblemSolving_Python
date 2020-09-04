'''
Problem Solving Baekjoon 16236
Author: Injun Son
Date: September 3, 2020
'''
from collections import deque
import sys

import sys
import copy
N = int(input())
graph = [ list(map(int, input().split())) for _ in range(N)]
fish_map = copy.deepcopy(graph)
shark_pos = [0,0]
count = 0
shark_size = 2
def get_shark_distance(y, x, shark_pos):
    return abs(y-shark_pos[0])+abs(x-shark_pos[1])

#상어 초기 위치 찾기
for i in range(N):
    for j in range(N):
        if graph[i][j]==9:
            shark_pos = [i,j]
            break

#물고기 지도 초기화하기
for i in range(N):
    for j in range(N):
        if 1<=graph[i][j]<=6:
            fish_map[i][j] = [graph[i][j], get_shark_distance(i, j, shark_pos)]


