'''
Problem Solving Baekjoon 16926
Author: Injun Son
Date: September 15, 2020
'''
from collections import deque
import heapq
import sys, copy

input = sys.stdin.readline
N, M, R = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def print_board(board):
    for i in range(N):
        for j in range(M):
            print(board[i][j], end=" ")
        print()

def rotate_graph():
    global graph
    graph2 = [ [0]*M for _ in range(N)]
    tmp_lst = [[] for _ in range(min(N, M) // 2)]
    for k in range(min(N, M)//2):
        cur_y, cur_x = k,k
        dir = 0
        # 시계방향으로 돌면서 쭉 저장
        while graph2[cur_y][cur_x]==0:
            tmp_lst[k].append(graph[cur_y][cur_x])
            graph2[cur_y][cur_x] = 1
            ny, nx = cur_y+dy[dir], cur_x+dx[dir]
            if (ny, nx)==(k,k):
                break
            if ny<0 or nx<0 or ny>=N or nx>=M or graph2[ny][nx] !=0:
                dir = (dir+1)%4
                ny, nx = cur_y+dy[dir], cur_x+dx[dir]

            cur_y, cur_x = ny, nx

    # print(tmp_lst)
    #회전 시켜준다
    for i in range(len(tmp_lst)):
        queue_lst = deque(tmp_lst[i])
        queue_lst.rotate(-R)
        tmp_lst[i] = list(queue_lst)

    # print(tmp_lst)
    graph2 = [[0] * M for _ in range(N)]

    for k in range(min(N, M)//2):
        cur_y, cur_x = k,k
        dir = 0
        i=0
        # 시계방향으로 돌면서 rotate된 배열을 다시 붙여준다
        while graph2[cur_y][cur_x]==0:
            # print(cur_y, cur_x, tmp_lst[k][i])
            graph[cur_y][cur_x] = tmp_lst[k][i]
            graph2[cur_y][cur_x] =1
            i +=1
            ny, nx = cur_y+dy[dir], cur_x+dx[dir]
            if (ny, nx)==(k,k):
                break
            if ny<0 or nx<0 or ny>=N or nx>=M or graph2[ny][nx] !=0:
                dir = (dir+1)%4
                ny, nx = cur_y+dy[dir], cur_x+dx[dir]

            cur_y, cur_x = ny, nx
    # print_board(graph)
    # print()

rotate_graph()
print_board(graph)
