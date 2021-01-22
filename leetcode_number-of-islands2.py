'''
Problem Solving leetcode number-of-islands
Author: Injun Son
Date: January 22, 2021
'''
import heapq
import sys
import collections
from typing import List
from collections import defaultdict
sys.setrecursionlimit(100000)
import re
from collections import deque
dx = [-1, 0, 0, 1]
dy = [0, 1, -1, 0]

visited = None

def numIslands(grid: List[List[str]]) -> int:
    global visited
    count = 0
    visited = [[0] * len(grid[0]) for _ in range(len(grid))]

    def dfs(y, x):
        visited[y][x] = 1
        for k in range(4):
            ny, nx = y + dy[k], x + dx[k]
            if 0<= ny <len(grid) and 0 <= nx <len(grid[0]):
                if grid[ny][nx] == "1" and visited[ny][nx] == 0:
                    dfs(ny, nx)

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "1" and visited[i][j] == 0:
                dfs(i, j)
                print_board(visited)
                count += 1

    return count

def print_board(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            print(board[i][j], end= " ")
        print()
    print()
print(numIslands([
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]))