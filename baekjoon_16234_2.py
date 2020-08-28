'''
Problem Solving Baekjoon 16234_2
Author: Injun Son
Date: August 28, 2020
'''
import sys, copy
from collections import deque

import sys
sys.setrecursionlimit(10000)
N, L, R = map(int, sys.stdin.readline().split())
maps = []
cnt = 0
for _ in range(N):
    maps.append(list(map(int, sys.stdin.readline().split())))

dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def bfs(maps, start, visited):
    # 조건을 충족하는 좌표들을 group에 저장한다
    group = set()
    group.add(start)
    queue = deque()
    queue.append(start)
    while queue:
        y, x = queue.popleft()
        visited[y][x]=1
        for dy, dx in dirs:
            ny, nx = y+dy, x+dx
            if 0<=ny<N and 0<=nx<N and not visited[ny][nx] and L<=abs(maps[y][x]-maps[ny][nx])<=R:
                visited[ny][nx] = 1
                group.add((ny, nx))
                queue.append((ny, nx))
    return group

while True:
    # maps 좌표 값이 변하는지 아닌지 확인
    prev_maps = copy.deepcopy(maps)
    visited = [[0 for _ in range(N)] for _ in range(N)]

    #bfs로 순회하면서 주건에 맞는 그룹을 저장
    groups = []
    for y in range(N):
        for x in range(N):
            if visited[y][x]==0:
                groups.append(bfs(maps, (y, x), visited))

    for each in groups:
        # 그룹이 있으면 len(each)가 0보다 크다
        if each:
            #update할 새 값 계산
            value = sum(maps[y][x] for y, x in each)// len(each)
            for y, x in each:
                maps[y][x] = value
    if prev_maps == maps:
        break
    cnt+=1
print(cnt)
