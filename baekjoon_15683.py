'''
Problem Solving Baekjoon 15683
Author: Injun Son
Date: August 30, 2020
'''
import sys, copy
from collections import deque

r, c = map(int, input().split())
graph = [ list(map(int, input().split())) for _ in range(r)]
cctvs = []
min_ans = sys.maxsize

# 북 동 남 서
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

for i in range(r):
    for j in range(c):
        if 1<= graph[i][j] <=5:
            cctvs.append([graph[i][j], i, j])

max_num = len(cctvs)
cctv = cctvs.append([])
def count_blind_spots(graph):
    count = 0
    for i in range(r):
        for j in range(c):
            if graph[i][j]==0:
                count +=1
    return count

def print_board(board):
    for i in range(r):
        for j in range(c):
            print(board[i][j], end=" ")
        print("")

def go_straight(map, y, x, dir):
    tmp_map = copy.deepcopy(map)
    ny, nx = y + dy[dir], x + dx[dir]
    while 0 <= ny < r and 0 <= nx < c and tmp_map[ny][nx] != 6:
        if 1 <= tmp_map[ny][nx] <= 5:
            ny, nx = ny + dy[dir], nx + dx[dir]
            continue
        else:
            tmp_map[ny][nx] = 7

        ny, nx = ny + dy[dir], nx + dx[dir]
    return tmp_map

def rotate_cctv(map, cctv_info):
    cctv_num = cctv_info[0]
    y, x = cctv_info[1], cctv_info[2]
    map_list = []
    if cctv_num==1:
        for i in range(4):
            map_list.append(go_straight(map, y, x, i))

    elif cctv_num==2:
        #가로
        tmp_map = go_straight(map, y, x, 1)
        tmp_map2 = go_straight(tmp_map, y, x, 3)
        map_list.append(tmp_map2)
        #세로
        tmp_map = go_straight(map, y, x, 0)
        tmp_map2 = go_straight(tmp_map, y, x, 2)
        map_list.append(tmp_map2)
    elif cctv_num==3:
        #위오른
        tmp_map = go_straight(map, y, x, 0)
        tmp_map2 = go_straight(tmp_map, y, x, 1)
        map_list.append(tmp_map2)
        #오른아래
        tmp_map = go_straight(map, y, x, 1)
        tmp_map2 = go_straight(tmp_map, y, x, 2)
        map_list.append(tmp_map2)
        #아래왼
        tmp_map = go_straight(map, y, x, 2)
        tmp_map2 = go_straight(tmp_map, y, x, 3)
        map_list.append(tmp_map2)
        #왼위
        tmp_map = go_straight(map, y, x, 3)
        tmp_map2 = go_straight(tmp_map, y, x, 0)
        map_list.append(tmp_map2)
    elif cctv_num==4:
        #왼위오
        tmp_map = go_straight(map, y, x, 3)
        tmp_map2 = go_straight(tmp_map, y, x, 0)
        tmp_map3 = go_straight(tmp_map2, y, x, 1)
        map_list.append(tmp_map3)
        #위오아래
        tmp_map = go_straight(map, y, x, 0)
        tmp_map2 = go_straight(tmp_map, y, x, 1)
        tmp_map3 = go_straight(tmp_map2, y, x, 2)
        map_list.append(tmp_map3)
        #오아래왼
        tmp_map = go_straight(map, y, x, 1)
        tmp_map2 = go_straight(tmp_map, y, x, 2)
        tmp_map3 = go_straight(tmp_map2, y, x, 3)
        map_list.append(tmp_map3)
        #아래왼위
        tmp_map = go_straight(map, y, x, 2)
        tmp_map2 = go_straight(tmp_map, y, x, 3)
        tmp_map3 = go_straight(tmp_map2, y, x, 0)
        map_list.append(tmp_map3)

    elif cctv_num==5:
        tmp_map = go_straight(map, y, x, 0)
        tmp_map2 = go_straight(tmp_map, y, x, 1)
        tmp_map3 = go_straight(tmp_map2, y, x, 2)
        tmp_map4 = go_straight(tmp_map3, y, x, 3)
        map_list.append(tmp_map4)

    return map_list

def back_tracking(cur_count, max_count, cctv_list, map):
    global min_ans
    if cur_count == max_count:
        if min_ans > count_blind_spots(map):
            pass
            # print_board(map)
            # print()
        min_ans = min(min_ans, count_blind_spots(map))
        return

    else:
        map_backup = copy.deepcopy(map)
        possible_maps = rotate_cctv(map_backup, cctv_list[cur_count])
        for possible_map in possible_maps:
            back_tracking(cur_count+1, max_count, cctv_list, possible_map)


back_tracking(0, max_num, cctvs, graph)
print(min_ans)
