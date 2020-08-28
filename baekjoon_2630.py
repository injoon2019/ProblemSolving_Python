'''
Problem Solving Baekjoon 2630
Author: Injun Son
Date: August 28, 2020
'''
import math, sys, copy
from collections import deque
sys.setrecursionlimit(10**6)
def divide_and_conquer(y, x, size):
    global white, blue
    all_same = True
    first_tile = graph[y][x]
    for i in range(y, y+size):
        for j in range(x, x+size):
            if graph[i][j] != first_tile:
                all_same = False

    if all_same:
        if first_tile==1:
            blue += 1
        else:
            white += 1

    else:
        divide_and_conquer( y, x, size//2)
        divide_and_conquer( y, x+size//2, size // 2)
        divide_and_conquer(y+size//2, x, size // 2)
        divide_and_conquer(y+size//2, x+size//2, size // 2)


N = int(input())
white, blue = 0, 0
graph = [list(map(int, input().split())) for _ in range(N)]

divide_and_conquer(0, 0, N)
print(white)
print(blue)