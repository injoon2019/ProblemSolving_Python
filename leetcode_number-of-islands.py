'''
Problem Solving leetcode number-of-islands
Author: Injun Son
Date: October 20, 2020
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


def numIslands(grid: List[List[str]]) -> int:
    def dfs(i, j):
        #더 이상 땅이 아닌 경우 종료
        if i<0 or i>=len(grid) or \
            j<0 or j >=len(grid[0]) or \
            grid[i][j] != '1':
            return

        grid[i][j] = 0
        #동서남북 탐색
        dfs(i+1, j)
        dfs(i-1, j)
        dfs(i, j+1)
        dfs(i, j-1)

    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                dfs(i, j)
                # 모든 육지 탐색 후 카운트 1 증가
                count +=1
    return count

print(numIslands([
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]))