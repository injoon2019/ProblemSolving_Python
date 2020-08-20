'''
Problem Solving Baekjoon 2186_2
Author: Injun Son
Date: August 19, 2020
'''
from collections import deque
import sys, copy
from itertools import permutations
dx = [-1, 0, 0, 1]
dy = [0, 1, -1, 0]

def dfs(x, y, idx):
    if idx == len(word):
        return 1
    #이미 부분적으로 탐색을 한적이 있으면, 그 결과값 반환
    if c[x][y][idx] != -1:
        return c[x][y][idx]

    #방문했다는 표시를 남기고
    c[x][y][idx] = 0
    for i in range(4):
        temp_x, temp_y = x, y
        for _ in range(k):
            nx = temp_x + dx[i]
            ny = temp_y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if a[nx][ny] == word[idx]:
                    #방문한 곳에 답 표시
                    c[x][y][idx] += dfs(nx, ny, idx+1)
            temp_x, temp_y = nx, ny
    return c[x][y][idx]
    

n, m, k = map(int, input().split())
a = []
for _ in range(n):
    a.append(list(input().strip()))
word = list(input().strip())

start = []
#dfs 후보들을 고른다
for i in range(n):
    for j in range(m):
        if a[i][j]==word[0]:
            start.append([i, j])

ans =  0
c = [[[-1] * len(word) for _ in range(m)] for _ in range(n)]
#후보들에 대하여 dfs 돌린다 
for i in range(len(start)):
    x, y = start[i]
    ans += dfs(x, y, 1)
print(ans)