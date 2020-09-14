'''
Problem Solving Baekjoon 14500_2
Author: Injun Son
Date: September 14, 2020
'''
from collections import deque
import sys

r, c = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(r)]

tetromino = [
    [(0,0), (0,1), (0,2), (0,3)],
    [(0,0), (1,0), (2,0), (3,0)],
    [(0,0), (0,1), (1,0), (1,1)],
    [(0,0), (1,0), (2,0), (2,1)],
    [(1,0), (1,1), (1,2), (0,2)],
    [(0,0), (0,1), (1,1), (2,1)],
    [(0,0), (0,1), (0,2), (1,0)],
    [(2,0), (2,1), (1,1), (0,1)],
    [(0,0), (0,1), (0,2), (1,2)],
    [(0,0), (0,1), (1,0), (2,0)],
    [(0,0), (1,0), (1,1), (1,2)],
    [(0,0), (1,0), (1,1), (2,1)],
    [(1,0), (1,1), (0,1), (0,2)],
    [(0,0), (0,1), (1,1), (1,2)],
    [(0,1), (1,0), (1,1), (2,0)],
    [(0,0), (0,1), (0,2), (1,1)],
    [(0,0), (1,0), (1,1), (2,0)],
    [(0,1), (1,0), (1,1), (1,2)],
    [(0,1), (1,0), (1,1), (2,1)]
]
ans = 0
def find(y, x):
    global ans
    for i in range(19):
        result = 0
        for j in range(4):
            try:
                ny= y+ tetromino[i][j][0]
                nx = x + tetromino[i][j][1]
                result += graph[ny][nx]
            except:
                break
        ans = max(ans, result)

for i in range(r):
    for j in range(c):
        find(i, j)

print(ans)