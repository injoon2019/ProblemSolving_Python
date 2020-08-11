'''
Problem Solving Baekjoon 1992
Author: Injun Son
Date: August 11, 2020
'''
import sys
from collections import deque

def is_allSame(y_start, x_start, size):
    global answer

    allSame = True
    start_num = graph[y_start][x_start]
    for i in range(y_start, y_start + size):
        for j in range(x_start, x_start + size):
            if graph[i][j] != start_num:
                allSame = False
                break

    if allSame ==False:
        answer.append("(")
        for i in range(2):
            for j in range(2):
                is_allSame(y_start+(i*(size//2)), x_start+(j*(size//2)), size//2)
        answer.append(")")
    if allSame:
        answer.append(str(start_num))


N = int(input())
graph = [list(input()) for _ in range(N)]
answer = []

is_allSame(0, 0, N)
for i in answer:
    print(i, end="")