'''
Problem Solving Baekjoon 2186_3
Author: Injun Son
Date: October 20, 2020
'''
from collections import deque
import sys, copy
from itertools import permutations

dx = [-1, 0, 0, 1]
dy = [0, 1, -1, 0]

def dfs(y, x, idx):
    if idx == len(word):
        return 1

    if dp[y][x][idx] != -1:
        return dp[y][x][idx]

    dp[y][x][idx] = 0
    for i in range(4):
        temp_y, temp_x = y, x
        for _ in range(k):
            ny, nx = temp_y+dy[i], temp_x+dx[i]
            if 0<=ny<r and 0<=nx<c:
                if graph[ny][nx] == word[idx]:
                    dp[y][x][idx] += dfs(ny, nx, idx+1)
            temp_y, temp_x = ny, nx
    return dp[y][x][idx]

r, c, k = map(int, input().split())
graph = [list(input()) for _ in range(r)]
word = list(input())
#DP[i][j][k] = "(i, j)에 존재하는 알파벳을 찾고자하는 문자열의 'k'번 인덱스로 설정했을 때, 나올 수 있는 정답의 갯수
dp = [[[-1]*len(word) for _ in range(c)] for _ in range(r)]
start = []
for i in range(r):
    for j in range(c):
        if graph[i][j] == word[0]:
            start.append([i,j])

ans = 0
for i in range(len(start)):
    y, x = start[i]
    ans += dfs(y, x, 1)

print(ans)