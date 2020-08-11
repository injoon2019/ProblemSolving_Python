'''
Problem Solving Baekjoon 2447
Author: Injun Son
Date: August 11, 2020
'''
import sys
def divide_and_conquer(start_y, start_x, size):
    global graph
    if size==1:
        graph[start_y][start_x]="*"
    else:
        for i in range(3):
            for j in range(3):
                if i==1 and j==1:
                    continue
                else:
                    divide_and_conquer(start_y+(i*(size//3)), start_x+(j*(size//3)), size//3)

N = int(input())
graph = [[" "]*N for _ in range(N)]

divide_and_conquer(0, 0, N)
for i in range(N):
    for j in range(N):
        print(graph[i][j], end="")
    print("")