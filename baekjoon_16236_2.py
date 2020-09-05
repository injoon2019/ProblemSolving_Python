'''
Problem Solving Baekjoon 16236_2
Author: Injun Son
Date: September 4, 2020
'''
from collections import deque
import sys
import heapq
import copy

n= int(input())
maps = []
for y in range(n):
    arr = list(map(int, sys.stdin.readline().split()))
    for x in range(len(arr)):
        if arr[x] == 9:
            start = (y,x,0)
    maps.append(arr)

def find_min_dist(start, maps, current_size):
    dirs = [(0,1), (0,-1), (1,0), (-1,0)]
    queue = deque()
    queue.append(start)

    y, x, cnt = start
    maps[y][x] = 0
    min_dist = []
    visited = set()
    while queue:
        y, x, cnt = queue.popleft()
        visited.add((y,x))
        for dy, dx in dirs:
            ny, nx = y+dy, x+dx
            if 0<=ny <len(maps) and 0<=nx<len(maps) and (ny, nx) not in visited:
                visited.add((ny, nx))
                # 다음 칸으로 이동할 수 있는 경우
                if maps[ny][nx]==0 or maps[ny][nx]==current_size:
                    queue.append((ny, nx, cnt+1))
                    continue
                # 지나갈 수 없는 경우
                if maps[ny][nx]>current_size:
                    continue
                else:
                    #먹을 수 있는 경우
                    heapq.heappush(min_dist, (cnt+1, ny, nx))

    #먹을 수 있는 후보군 중 조건에 부합하는 것
    if min_dist:
        return min_dist[0]
    else:
        return None

time = 0
current_size = 2
already_eat=0

while True:
    next_value = find_min_dist(start, maps, current_size)
    # 더 이상 먹을 수 있는 물고기가 없는 경우
    if next_value is None:
        break
    #cnt= 다음 물고기를 먹기까지 걸린 시간
    cnt, ny, nx = next_value
    time += cnt

    #먹은 물고기 개수를 센다
    already_eat +=1

    if already_eat ==current_size:
        current_size +=1
        already_eat = 0

    #다음 출발점을 정한다
    start = (ny, nx, 0)

print(time)