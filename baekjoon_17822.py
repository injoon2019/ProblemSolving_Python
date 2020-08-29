'''
Problem Solving Baekjoon 17822
Author: Injun Son
Date: August 29, 2020
'''
from collections import deque
# N은 원판의 개수 M은 원판에 적혀있는 정수의 개수 T는 회전수
N, M, T = map(int, input().split())
circles = [[0]*M for _ in range(N+1)]
rotates = [ [] for _ in range(T+1)]

dx = [-1, 0, 0, 1]
dy = [0, 1, -1, 0]

def print_board():
    for i in range(1, N+1):
        for j in range(M):
            print(circles[i][j], end=" ")
        print("")
    print("")

def bfs(y, x):
    visited_check[y][x] = 1
    q = deque()
    q.append([y, x])
    group = set()
    group.add((y, x))
    while q:
        y, x  = q.popleft()
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if nx==M:
                nx =0
            if nx==-1:
                nx = M-1
            if 1<=ny<N+1 and visited_check[ny][nx] == 0:
                if circles[y][x] == circles[ny][nx]:
                    group.add((ny, nx))
                    visited_check[ny][nx] = 1
                    q.append([ny, nx])
    return group

def get_count_sum():
    total_count = 0
    total_sum = 0
    for i in range(1, N+1):
        for j in range(M):
            if circles[i][j]!=0:
                total_count+=1
                total_sum += circles[i][j]

    return total_count, total_sum

def change_elements(average):
    for i in range(1, N+1):
        for j in range(M):
            if circles[i][j]!=0:
                if circles[i][j] < average and circles[i][j]!=0:
                    circles[i][j] +=1
                elif circles[i][j] > average:
                    circles[i][j] -=1

'''
    a
 d     b
    b
'''
for i in range(1, N+1):
    tmp_list = list(map(int, input().split()))
    for k in tmp_list:
        circles[i] = tmp_list

#T개만큼 회전 방법들을 받는다
for t in range(1, T+1):
    x, d, k = map(int, input().split())
    rotates[t]=[x,d,k]

#T번 진행한다
for t in range(1, T+1):
    x, d, k = rotates[t]
    # if t==4:
    #     print("fuck", x, d, k)
    groups = []
    # x의 배수인 원판을 d방향으로 k칸 회전시킨다
    for n in range(1, N+1):
        if n%x ==0:
            # d가 0인 경우는 시계방향, 1이면 반시계
            if d==0:
                circles[n]=deque(circles[n])
                circles[n].rotate(k)
                circles[n] = list(circles[n])
            else:
                circles[n]=deque(circles[n])
                circles[n].rotate(-k)
                circles[n] = list(circles[n])
                # if t==4:
                #     print("check")
                # print_board()

    visited_check = [[0]*M for _ in range(N+1)]

    for i in range(1, N+1):
        for j in range(M):
            if not visited_check[i][j] and circles[i][j]!=0:
                groups.append(bfs(i, j))

    changed = False
    # print("print group", groups)

    for group in groups:
        if len(group) > 1:
            changed = True
            for coordinate in group:
                y, x = coordinate[0], coordinate[1]
                circles[y][x] = 0

    if not changed:
        total_count, total_sum = get_count_sum()
        if total_count !=0:
            change_elements(total_sum/total_count)

    # print_board()
_, ans = get_count_sum()
print(ans)