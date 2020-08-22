'''
Problem Solving Baekjoon 1261
Author: Injun Son
Date: August 21, 2020
'''
import sys
from heapq import heappush, heappop
INF = sys.maxsize
dx = [-1, 0, 0, 1]
dy = [0, 1, -1, 0]

def print_board():
    for i in range(r):
        for j in range(c):
            print(cost_graph[i][j], end=" ")
        print("")

def dijkstra():
    global cost_graph
    heap = []
    heappush(heap, [0, 0, 0]) #weight, y, x
    cost_graph[0][0] = 0
    while heap:
        cost, y, x = heappop(heap)
        for i in range(4):
            ny = y+dy[i]
            nx = x+dx[i]
            if 0<=ny<r and 0<=nx<c:
                if graph[ny][nx]=='0':
                    if cost_graph[ny][nx] > cost_graph[y][x] and cost_graph[ny][nx]==INF:
                        cost_graph[ny][nx] = cost_graph[y][x]
                        heappush(heap, [cost_graph[ny][nx], ny, nx])

                else:
                    #벽을 깨고 가는 것이 더 유리한 상황
                    if cost_graph[ny][nx] > cost_graph[y][x]+1:
                        cost_graph[ny][nx] = cost_graph[y][x]+1
                        heappush(heap, [cost_graph[ny][nx], ny, nx])
                        graph[ny][nx]='0'


c, r = map(int, input().split())
graph = [list(input()) for _ in range(r)]
cost_graph = [[INF]*c for _ in range(r)]
dijkstra()
print(cost_graph[r-1][c-1])