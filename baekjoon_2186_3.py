'''
Problem Solving Baekjoon 2186_3
Author: Injun Son
Date: October 20, 2020
'''
from collections import deque
import sys, copy
from itertools import permutations

dy = [-1, 0, 0, 1]
dx = [0, 1, -1, 0]

def dfs(y, x, idx):
    if idx == len(word):
        return 1
    if c[y][x][idx] != -1:
        return c[y][x][idx]

    c[y][x][idx] = 0
    for i in range(4):
        temp_y, temp_x = y, x
        for _ in range(k):
            ny = temp_y + dy[i]
            nx = temp_x + dx[i]
            if 0<= ny< n and 0<=nx < m:
                if a[ny][nx] == word[idx]:
                    c[y][x][idx] += dfs(ny, nx, idx+1)
            temp_y, temp_x = ny, nx
    return c[y][x][idx]


n, m, k = map(int, input().split())
a = []
for _ in range(n):
    a.append(list(input().strip()))
word = list(input().strip())

start = []
# dfs 후보들을 고른다
for i in range(n):
    for j in range(m):
        if a[i][j]==word[0]:
            start.append([i,j])

ans = 0
#DP[i][j][k] = "(i, j)에 존재하는 알파벳을 찾고자하는 문자열의 'k'번 인덱스로 설정했을 때, 나올 수 있는 정답의 갯수
c = [[[-1]*len(word) for _ in range(m)] for _ in range(n)]

for i in range(len(start)):
    y, x = start[i]
    ans += dfs(y, x, 1)
print(ans)