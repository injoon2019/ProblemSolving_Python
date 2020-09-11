'''
Problem Solving Baekjoon 2206
Author: Injun Son
Date: September 11, 2020
'''
import sys
from heapq import heappop, heappush
import copy
from collections import deque
import heapq
height, width = map(int, sys.stdin.readline().split())
maps= []
for _ in range(height):
    maps.append(sys.stdin.readline())

# 벽을 부수고 방문했는지, 아닌지에 따라 최단거리가 달라질 수 있으므로
# visited는 부수지 않고 지나감 / 부수고 지나감 두 가지가 필요하다
# 따라서 visited[y][x][벽 파괴여부]

visited = [[[0]*2 for _ in range(width)] for _ in range(height)]

def bfs(start, maps, visited, height, width):
    dirs = [(0,1), (1,0), (0,-1), (-1,0)]
    queue = []
    # 최단거리일수록 우선 뽑기 위해 heapq 사용
    heapq.heappush(queue, start)
    while queue:
        cnt, wall, y, x = heapq.heappop(queue)
        visited[y][x][wall] = 1
        # 목적지에 도착했을 경우 cnt를 리턴
        if y==height -1 and x==width-1:
            return cnt

        for dy, dx in dirs:
            ny, nx = y+dy, x+dx
            if 0<=ny<height and 0<=nx<width and visited[ny][nx][wall]==0:
                if maps[ny][nx]=='0' or (maps[ny][nx]=='1' and wall==0):
                    visited[ny][nx][wall] =1
                    #벽을 부수는 경우
                    if maps[ny][nx]=="1":
                        heapq.heappush(queue, (cnt+1, wall+1, ny, nx))
                    else:
                        heapq.heappush(queue, (cnt+1, wall, ny, nx))
    return -1

#시작점부터 1을 세고 시작한다
print(bfs((1,0,0,0), maps, visited, height, width))

