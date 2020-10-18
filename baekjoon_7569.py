'''
Problem Solving Baekjoon 7569
Author: Injun Son
Date: October 18, 2020
'''

from collections import deque
import sys
import math
import copy

width, height, depth = map(int, input().split())
maps = []
starts = []
no_zero = True

def bfs(starts, maps, depth, height, width):
    #가로, 세로, 높이로 각각 이동
    dirs = [(1,0,0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
    queue = deque()
    queue.extend(starts)
    while queue:
        cd, ch, cw, cnt = queue.popleft()
        for dd, dh, dw in dirs:
            nd, nh, nw = cd+dd, ch+dh, cw+dw
            if 0<=nh<height and 0<=nd<depth and 0<=nw<width and maps[nd][nh][nw]==0:
                maps[nd][nh][nw] = 1
                queue.append((nd, nh, nw, cnt+1))
    return cnt


#토마토가 bfs후 다 익었는지 아닌지 체크
def check(maps, depth, height, width):
    for d in range(depth):
        for h in range(height):
            for w in range(width):
                if maps[d][h][w] == 0:
                    return -1
    return 0

for d in range(depth):
    temp = []
    for h in range(height):
        a = list(map(int, input().split()))
        for w in range(width):
            if a[w]==0:
                no_zero = False
            if a[w] == 1:
                starts.append((d, h, w, 0))
        temp.append(copy.deepcopy(a))
    maps.append(copy.deepcopy(temp))

#처음부터 0이 하나도 없을 경우 더 계산할 필요가 없다
if no_zero:
    print(0)
    exit()

count = bfs(starts, maps, depth, height, width)

if check(maps, depth, height, width) != 0:
    print(-1)
else:
    print(count)