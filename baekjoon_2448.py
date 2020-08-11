'''
Problem Solving Baekjoon 2448
Author: Injun Son
Date: August 11, 2020
'''
import sys
N = int(input())
graph = [[" "]*(2*N -1) for i in range(N)]

def divide_and_conquer(start_y, start_x, size):
    if size==3:
        graph[start_y][start_x]="*"
        graph[start_y+1][start_x-1] =  graph[start_y+1][start_x+1]= "*"
        graph[start_y + 2][start_x - 2] = graph[start_y + 2][start_x - 1] = graph[start_y + 2][start_x] = "*"
        graph[start_y + 2][start_x + 1] = graph[start_y + 2][start_x+2] = "*"
    else:
        divide_and_conquer(start_y, start_x, size//2)
        divide_and_conquer(start_y+size//2, start_x-size//2, size // 2)
        divide_and_conquer(start_y+size//2, start_x+size//2, size // 2)

divide_and_conquer(0, N-1, N)
answer = ""
for i in range(N):
    print("".join(graph[i]), sep="")