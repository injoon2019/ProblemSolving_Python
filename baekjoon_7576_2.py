'''
Problem Solving Baekjoon 7576_2
Author: Injun Son
Date: July 31, 2020
'''
import sys
from collections import deque
sys.setrecursionlimit(100000)

dx = [-1, 0, 0, 1]
dy = [0, 1, -1, 0]
w, h = map(int, sys.stdin.readline().rstrip().split())

arr = [list(map(int, input().split())) for _ in range (h)]

q = deque()
for i in range(h):
    for j in range(w):
        if arr[i][j]==1:
            q.append([i,j])

def bfs():
    global q
    while q:
        now = q.popleft()
        for i in range(4):
            ny = now[0]+ dy[i]
            nx = now[1]+ dx[i]
            if 0<=ny<h and 0<=nx<w:
                if arr[ny][nx]==0:
                    arr[ny][nx] = arr[now[0]][now[1]]+1
                    q.append([ny, nx])

def get_answer():
    ans = 0
    for i in range(h):
        for j in range(w):
            a = arr[i][j]
            if a==0:
                #bfs 돌고도 0이면 익지 않는 것이다
                print(-1)
                return
            ans = max(ans, a)
    #각 칸의 숫자 - 1은 전파되기까지 며칠이 소요됐는가를 나타낸다
    print(ans-1)

bfs()
get_answer()

