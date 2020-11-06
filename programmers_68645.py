'''
Problem Solving Programmers 68645
Author: Injun Son
Date: November 6, 2020
'''
import math
from itertools import combinations

dir = 0
dx = [0, 1, -1]
dy = [1, 0, -1]

def solution(n):
    global dir
    dir = 0
    answer = []
    graph = [[0]*n for _ in range(n)]
    cur_y, cur_x = 0, 0
    for i in range(1, (n*(n+1)//2) +1 ):
        graph[cur_y][cur_x] = i
        ny, nx = cur_y + dy[dir], cur_x + dx[dir]
        if 0<=ny<n and 0<=nx<ny+1 and graph[ny][nx]==0:
            cur_y, cur_x = ny, nx
        else:
            dir = (dir+1) % 3
            cur_y, cur_x = cur_y +dy[dir], cur_x + dx[dir]

    for i in range(n):
        for j in range(n):
            if graph[i][j]!=0:
                answer.append(graph[i][j])
            else:
                break
    return answer

print(solution(4))
print(solution(5))
print(solution(6))