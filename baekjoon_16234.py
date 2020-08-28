'''
Problem Solving Baekjoon 16234
Author: Injun Son
Date: August 28, 2020
'''
import sys, copy
from collections import deque

sys.setrecursionlimit(10**6)
N, L, R = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
ans = 0
group = 1
def print_board(board):
    for i in range(N):
        for j in range(N):
            print(board[i][j], end=" ")
        print("")

def bfs1(y, x):
    global group
    queue = deque()
    graph_group[y][x] = group
    # 그 그룹에 몇개가 있는지
    group_count_sum[group][0] += 1
    # 그 그룹에 인구가 얼마나 있는지
    group_count_sum[group][1] += graph[y][x]
    queue.append([y, x])
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if 0<=nx<N and 0<=ny<N and graph_group[ny][nx]==0:
                if L<= abs(graph[y][x] -graph[ny][nx]) <=R:
                    graph_group[ny][nx] = group
                    group_count_sum[group][0] += 1
                    group_count_sum[group][1] += graph[ny][nx]
                    queue.append([ny, nx])
def bfs(y, x):
    global averaged_check, graph_group, graph
    queue = deque()
    averaged_check[y][x] = 1
    graph[y][x] = group_count_sum[graph_group[y][x]][1] // group_count_sum[graph_group[y][x]][0]
    queue.append([y, x])
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if 0<=ny<N and 0<=nx<N and averaged_check[ny][nx]==0 and graph_group[ny][nx]== graph_group[y][x]:
                graph[ny][nx] = graph[y][x]
                averaged_check[ny][nx] = 1
                queue.append([ny, nx])


while True:
    graph_group = [[0] * N for _ in range(N)]
    averaged_check = [[0]*N for _ in range(N)]
    # group_count_sum = [[0, 0]] * ((N**2)+1)
    group_count_sum = [[0]*2 for _ in range(N*N +1)]
    graph_backup = copy.deepcopy(graph)
    group = 1
    changed = False
    #그룹화하고 그룹별 갯수, 인구수 구하기
    for i in range(N):
        for j in range(N):
            if graph_group[i][j]==0:
                bfs1(i, j)
                group +=1

    #인구 이동시키기
    for i in range(N):
        for j in range(N):
            original_val = graph[i][j]
            if averaged_check[i][j]==0:
                bfs(i, j)
            if original_val != graph[i][j]:
                changed = True

    if changed:
        break
    else:
        ans +=1

print(ans)

'''
1, dfs 를 돌려서 그룹화하자
2, 그룹별로 이동을시키자(bfs로)
이걸 반복하되 1,2에서 변화가 없으면 그만하자
시간 초과났다
-통과한 코드의 차이점: 인구수를 이동시키는 부분에서 2중 for문을 써서 실패했다. 통과한 코드는 set로 바뀐 좌표들의 그룹을 행렬별로 묶어, 바뀐 것들만 따로 처리해주었다. 
'''

