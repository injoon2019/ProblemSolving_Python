'''
Problem Solving Baekjoon 19238
Author: Injun Son
Date: September 14, 2020
'''
from collections import deque
import heapq
import sys

N, M, fuel = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
start_y, start_x = map(int, input().split())
start_y -=1
start_x -=1
customer_start = []
customer_arrival = []

dy = [-1, 0, 0, 1, 0]
dx = [0, 1, -1, 0, 0]

def find_min_dist_to_customer(start_y, start_x):
    queue = deque()
    cnt = 0
    queue.append((0, start_y, start_x))
    min_dist = []
    visited = set()

    if (start_y, start_x) in customer_start:
        heapq.heappush(min_dist, (cnt, start_y, start_x,))

    visited.add((start_y, start_x))
    while queue:
        cnt, y, x = queue.popleft()
        for i in range(5):
            ny, nx = y+dy[i], x+dx[i]
            if 0<=nx<N and 0<=ny<N and (ny, nx) not in visited:
                #벽인 경우
                visited.add((ny, nx))
                if graph[ny][nx]==1:
                    continue
                else:
                    if (ny,nx) in customer_start:
                        #연료보다 거리가 더 먼 경우
                        if cnt > fuel:
                            continue
                        else:
                            visited.add((y, x))
                            heapq.heappush(min_dist, (cnt+1, ny, nx, ))
                            queue.append((cnt+1, ny, nx))
                    else:
                        visited.add((ny, nx))
                        queue.append((cnt+1, ny, nx))

    if min_dist:
        return min_dist[0]
    else:
        return None

def find_min_dist_to_dest(y, x, dest_y, dest_x):
    queue = deque()
    cnt = 0
    queue.append([cnt, y, x])
    visited= set()
    while queue:
        cnt, y, x = queue.popleft()
        if (y,x) == (dest_y, dest_x):
            return cnt
        else:
            for i in range(5):
                ny, nx = y+dy[i], x+dx[i]
                if 0<=ny<N and 0<=nx<N and graph[ny][nx] !=1 and (ny,nx) not in visited:
                    visited.add((ny, nx))
                    queue.append((cnt+1, ny, nx))
    return -100

for _ in range(M):
    a, b, c, d = map(int, input().split())
    customer_start.append((a-1, b-1))
    customer_arrival.append((c-1, d-1))

for _ in range(M):
    nearest = find_min_dist_to_customer(start_y, start_x)
    # print(customer_start)
    # print(customer_arrival)
    # print("fuel", fuel)
    # print("start pos", nearest[1], nearest[2])


    #아무 손님에게도 도달 못한 경우다
    if nearest == None:
        print("-1")
        exit()

    dest_index = customer_start.index((nearest[1], nearest[2]))
    dest_y, dest_x = customer_arrival[dest_index][0], customer_arrival[dest_index][1]
    fuel -= nearest[0]
    # print("fuel at start", fuel)

    dist = find_min_dist_to_dest(nearest[1], nearest[2], dest_y, dest_x)
    #목적지까지 도달 못한 경우
    if dist > fuel:
        # print("dist fuck", dist, fuel)
        print("-1")
        exit()
    fuel -= dist
    fuel += (dist*2)
    start_y, start_x = customer_arrival[dest_index][0],customer_arrival[dest_index][1]
    # print("destination pos", customer_arrival[dest_index][0], customer_arrival[dest_index][1])
    customer_start.pop(dest_index)
    customer_arrival.pop(dest_index)

    # print("fuel at dest", fuel)
    # print("---------------")

    if len(customer_start)==0:
        break

print(fuel)

'''
1. 87퍼정도에서 틀리는데 반례를 못찾겠다. 다른 사람 풀이를 봐야겠다. 
2. 아기상어 문제와 비슷한 점이 많다.
3. 여러 목표가 있을때 bfs 를 각각 돌리는 것이 아니라 한번 돌때 전체를 돌려서 해당 목표들까지 거리를 heap에 저장해두는 것.
4. heap에 (거리, y, x) 이런 식으로 저장을 해두면 거리가 최소인 것, 그리고 그 중에서도 가장 위에 왼쪽 것을 얻을 수 있다. 

'''




