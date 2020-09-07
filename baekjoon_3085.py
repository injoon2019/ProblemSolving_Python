'''
Problem Solving Baekjoon 3085
Author: Injun Son
Date: September 7, 2020
'''
import sys
from collections import deque

N = int(input())
graph = [list(input()) for _ in range(N)]
max_ans = -1*sys.maxsize

dx = [-1, 0, 0, 1]
dy = [0, 1, -1, 0]

def print_board():
    for i in range(N):
        for j in range(N):
            print(graph[i][j], end=" ")
        print("")
    print()

def count_func():
    global max_ans
    #row에 대해 count 하기
    for i in range(N):
        cur_count = 1
        longest_cont = 1
        for j in range(N):
            if j==0:
                cur_ch = graph[i][j]
                continue
            if graph[i][j]==cur_ch:
                cur_count +=1
                longest_cont = max(longest_cont, cur_count)
            else:
                cur_count=1
                cur_ch = graph[i][j]

        if max_ans < longest_cont:
            max_ans = max(max_ans, longest_cont)
            # print("row longest_count", longest_cont)
            # print_board()

    #column에 대해 count하기
    for j in range(N):
        cur_count = 1
        longest_cont = 1
        for i in range(N):
            if i==0:
                cur_ch = graph[i][j]
                continue
            if graph[i][j]==cur_ch:
                cur_count +=1
                longest_cont = max(longest_cont, cur_count)
            else:
                cur_count=1
                cur_ch = graph[i][j]

        if max_ans < longest_cont:
            max_ans = max(max_ans, longest_cont)
            # print("column, longest_count", longest_cont)
            # print_board()

count_func()
def change_adj(y, x):
    for i in range(4):
        ny, nx = y+dy[i], x+dx[i]
        if 0<=nx<N and 0<=ny<N:
            graph[y][x], graph[ny][nx] = graph[ny][nx], graph[y][x]
            count_func()
            graph[y][x], graph[ny][nx] = graph[ny][nx], graph[y][x]

for i in range(N):
    for j in range(N):
        change_adj(i, j)

print(max_ans)
