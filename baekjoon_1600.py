'''
Problem Solving Baekjoon 1600
Author: Injun Son
Date: October 25, 2020
'''
import sys
import datetime
from collections import deque
sys.setrecursionlimit(10**5)

dx1 = [-1, 0, 0, 1]
dy1 = [0, 1, -1, 0]

dx2 = [1, 2, 2, 1, -1, -2, -2, -1]
dy2 = [2, 1, -1, -2, -2, -1, 1, 2]

K = int(input())
C, R = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(R)]
dp = [ [[sys.maxsize]*(K+1) for _ in range(C)] for _ in range(R)]
min_move = sys.maxsize

def print_board():
    for i in range(R):
        for j in range(C):
            print(graph[i][j], end=" ")
        print()
    print()

# def dfs(left_k, y, x, move_count):
#     global min_move
#     if y==R-1 and x==C-1:
#         min_move = min(min_move, move_count)
#         return
#
#     dp[y][x][left_k] = move_count
#     if left_k:
#         for i in range(8):
#             ny, nx = y+dy2[i], x+dx2[i]
#             if 0<=ny<R and 0<=nx<C and graph[ny][nx]!= 1:
#                 if move_count+1 < dp[ny][nx][left_k-1]:
#                     dfs(left_k-1, ny, nx, move_count+1)
#     #근접이동
#     for i in range(4):
#         ny, nx = y+dy1[i], x+dx1[i]
#         if 0<=ny<R and 0<=nx<C and graph[ny][nx]!= 1:
#             if move_count+1 < dp[ny][nx][left_k]:
#                 dfs(left_k, ny, nx, move_count+1)

def bfs(K):
    global min_move
    q = deque()
    # left_k, y, x, move_count
    q.append([K, 0, 0, 0])
    dp[0][0][K] = 0
    while q:
        left_k, y, x, move_count = q.popleft()
        if y==R-1 and x==C-1:
            min_move = min(min_move, move_count)
            return

        if left_k:
            for i in range(8):
                ny, nx = y+dy2[i], x+dx2[i]
                if 0<=ny<R and 0<=nx<C and graph[ny][nx]!= 1:
                    if move_count+1 < dp[ny][nx][left_k-1]:
                        dp[ny][nx][left_k-1] = move_count+1
                        q.append([left_k-1, ny, nx, move_count+1])

        #근접이동
        for i in range(4):
            ny, nx = y+dy1[i], x+dx1[i]
            if 0<=ny<R and 0<=nx<C and graph[ny][nx]!= 1:
                if move_count+1 < dp[ny][nx][left_k]:
                    dp[ny][nx][left_k] = move_count + 1
                    q.append([left_k, ny, nx, move_count+1])

# print_board()
bfs(K)
print(min_move) if min_move != sys.maxsize else print(-1)