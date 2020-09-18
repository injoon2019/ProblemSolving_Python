'''
Problem Solving Baekjoon 17142
Author: Injun Son
Date: September 18, 2020
'''
import sys
import copy
from itertools import combinations
from collections import deque

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
virus_list = []

dx = [-1, 0, 0, 1]
dy = [0, 1, -1, 0]

def print_board(graph):
    for i in range(N):
        for j in range(N):
            print(graph[i][j], end=" ")
        print()
    print()

def bfs(graph_copy, virus_pos):
    q = deque()
    visited_check = dict()
    new_count =0
    for pos in virus_pos:
        q.append([pos[0], pos[1], 0])
        visited_check[(pos[0], pos[1])] = 1

    while q:
        y, x, cnt = q.popleft()
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if 0<=ny<N and 0<=nx<N and (ny, nx) not in visited_check and graph_copy[ny][nx] !='*' and graph_copy[ny][nx] !='-':
                visited_check[(ny, nx)]=1
                graph_copy[ny][nx] = cnt +1
                q.append([ny, nx, cnt+1])
                new_count +=1

    #다 전파시키고 나서 가장 큰 값이랑, 0의 개수 count 하기
    zero_count = 0
    max_val = -1
    for i in range(N):
        for j in range(N):

            if graph_copy[i][j] not in ['*', '-'] and graph_copy[i][j] > max_val:
                max_val = graph_copy[i][j]
            if graph_copy[i][j]==0:
                zero_count +=1

    return max_val, zero_count, new_count


#그래프를 돌면서 벽과, 바이러스를 놓을 수 있는 위치를 탐색해보자
for i in range(N):
    for j in range(N):
        if graph[i][j]==2:
            virus_list.append([i,j])
        if graph[i][j]==1:
            graph[i][j]='-'

possible_combs = list(combinations(virus_list, M))

min_ans = sys.maxsize

for comb in possible_combs:
    graph_copy = copy.deepcopy(graph)
    virus_list_copy = copy.deepcopy(virus_list)

    for pos in comb:
        #바이러스 설치한 자리는 '*' 표시해준다
        graph_copy[pos[0]][pos[1]] = '*'
        #바이러스 설치 가능 장소에서 설치했으면 제거한다
        virus_list_copy.remove(pos)

    #바이러스 설치 가능했지만 설치안됐으면 빈 칸으로 바꿔준다
    for pos in virus_list_copy:
        graph_copy[pos[0]][pos[1]] = 0

    # print_board(graph_copy)
    #바이러스 퍼뜨리는 것 진행해!
    max_val, zero_count, new_count = bfs(graph_copy, comb)
    # print(max_val, zero_count)
    if zero_count == 0 and max_val < min_ans:
        min_ans = max_val
        new = new_count

if min_ans != sys.maxsize:
    if min_ans==-1:
        print(0)
    else:
        print(min_ans)
else:
    print(-1)