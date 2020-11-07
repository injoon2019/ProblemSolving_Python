'''
Problem Solving Programmers woowa 4
Author: Injun Son
Date: November 7, 2020
'''
import math
from itertools import combinations
from itertools import combinations
from collections import deque

cur_y, cur_x = 0, 0
def solution(n, board):
    answer = 0
    global cur_y, cur_x
    cur_y, cur_x = 0, 0
    dx = [-1, 0, 0, 1]
    dy = [0, 1, -1, 0]

    def bfs(target):
        global cur_y, cur_x
        queue = deque()
        queue.append([cur_y, cur_x, 0])
        visited = [[0]*n for _ in range(n)]
        visited[cur_y][cur_x] = 1
        while queue:
            y, x, cnt = queue.popleft()
            if board[y][x] == target:
                cur_y, cur_x = y, x
                return cnt

            for i in range(4):
                ny, nx = y + dy[i], x+dx[i]

                if ny<0:
                    ny = n-1
                if ny>=n:
                    ny = 0
                if nx<0:
                    nx = n-1
                if nx >= n:
                    nx = 0

                visited[ny][nx] = 1
                queue.append([ny, nx, cnt+1])
    for i in range(1, (n*n) +1):
        answer += bfs(i)
        answer +=1 # 엔터키 누르는 것
    return answer

print(solution(3, [[3, 5, 6], [9, 2, 7], [4, 1, 8]]))
print(solution(2, [[2, 3], [4, 1]]))
print(solution(4, 	[[11, 9, 8, 12], [2, 15, 4, 14], [1, 10, 16, 3], [13, 7, 5, 6]]))