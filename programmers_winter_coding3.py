'''
Problem Solving Programmers winter_coding_3
Author: Injun Son
Date: October 31, 2020
'''
import math
from collections import deque
from itertools import combinations

def print_board(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            print(board[i][j], end=" ")
        print()
    print()


def solution(v):
    answer = [0, 0, 0]
    graph = v
    # print_board(graph)
    visited = [[-1]*len(graph[0]) for _ in range(len(graph))]

    dx = [-1, 0, 0, 1]
    dy = [0, 1, -1, 0]

    def bfs(y, x):
        visited[y][x] = graph[y][x]
        queue = deque()
        queue.append([y, x, graph[y][x]])

        while queue:
            y, x, food = queue.popleft()
            for i in range(4):
                ny, nx = y+dy[i], x+dx[i]
                if 0<=ny<len(graph) and 0<=nx<len(graph[0]) and food == graph[ny][nx] and visited[ny][nx]==-1:
                    visited[ny][nx] = food
                    queue.append([ny, nx, food])

    for i in range(len(graph)):
        for j in range(len(graph[0])):
            if visited[i][j]==-1:
                answer[graph[i][j]]+=1
                bfs(i, j)
    return answer

print(solution([[0,0,1,1],[1,1,1,1],[2,2,2,1],[0,0,0,2]]))
print(solution([[0,0,1],[2,2,1],[0,0,0]]))