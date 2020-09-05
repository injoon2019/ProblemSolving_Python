'''
Problem Solving Baekjoon 16236
Author: Injun Son
Date: September 4, 2020
'''
from collections import deque
import sys
import heapq
import copy
N = int(input())
graph = [ list(map(int, input().split())) for _ in range(N)]
shark_pos = [0,0]
count = 0
shark_size = 2
fish_list = []
fish_eat = 0
total_count = 0
dx = [-1, 0, 0, 1]
dy = [0, 1, -1, 0]

#상어 초기 위치 찾기
for i in range(N):
    for j in range(N):
        if graph[i][j]==9:
            shark_pos = [i,j]
            graph[i][j]=0
        elif 1<= graph[i][j] <=6:
            fish_list.append([graph[i][j], i, j ])

def print_board():
    print(shark_size)
    for i in range(N):
        for j in range(N):
            print(graph[i][j], end=" ")
        print("")
    print("")

#내가 원래 짠 코드대로 크기가 작은 물고기들의 위치마다 bfs를 돌리면 비효율적이다
#bfs를 한번돌리면서 먹을 수 있는 물고기들을 다 저장하는 것이 훨씬 효율적이다
def bfs(ty, tx):
    q = deque()
    # visited를 그래프를 copy하니 메모리초과, 시간초과다
    # set를 쓰면 훨씬 비용을 줄일 수 있다
    visited = set()
    y, x = shark_pos[0], shark_pos[1]
    cnt = 0
    visited.add((y,x))
    q.append([y, x, cnt])
    while q:
        y, x, cnt= q.popleft()
        if y== ty and x==tx:
            return cnt
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if 0<=nx<N and 0<=ny<N and graph[ny][nx]<=shark_size and (ny,nx) not in visited:
                visited.add((ny,nx))
                q.append([ny, nx, cnt+1])
    #만약 도달하는 방법이 없으면
    return sys.maxsize

#리스트를 쓰면 비효율적..
def fish_list_update():
    global fish_list
    i=0
    while i < len(fish_list):
        if fish_list[i][0]<shark_size:
            fish_distance = bfs(fish_list[i][1], fish_list[i][2])
        else:
            fish_distance = sys.maxsize
        if len(fish_list[i])>3:
            fish_list[i].pop()
        fish_list[i].append(fish_distance)
        i+=1
    fish_list = sorted(fish_list ,key = lambda x: (x[3], x[1], x[2], x[0]) )
    #fish_list = [물고기크기, y좌표, x좌표, 물고기까지 가는데 거리]


while True:
    fish_list_update()
    if len(fish_list)==0:
        break
    i=0
    while i < len(fish_list):
        if fish_list[i][0] < shark_size and fish_list[i][3] != sys.maxsize:
            shark_pos = [fish_list[i][1], fish_list[i][2]]
            fish_eat+=1
            if fish_eat==shark_size:
                shark_size+=1
                fish_eat=0
            graph[fish_list[i][1]][fish_list[i][2]]=0
            total_count += fish_list[i][3]
            fish_list = fish_list[1:]
            fish_list_update()
            i=0
        else:
            print(total_count)
            exit()

print(total_count)

