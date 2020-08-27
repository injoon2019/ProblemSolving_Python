'''
Problem Solving Baekjoon 2210
Author: Injun Son
Date: August 26, 2020
'''
import math, sys
# 위 오른 아래 왼
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

possible_nums = set()
graph = [list(map(int, input().split())) for _ in range(5)]

def dfs(y, x, cnt, num):
    if cnt == 5:
        possible_nums.add(num)
        return

    for i in range(4):
        ny, nx = y+dy[i], x+dx[i]
        if 0>ny or ny>=5 or 0>nx or nx>=5:
            continue
        dfs(ny, nx, cnt+1, num*10+graph[ny][nx])

for i in range(5):
    for j in range(5):
        dfs(i, j, 0, graph[i][j])

print(len(possible_nums))