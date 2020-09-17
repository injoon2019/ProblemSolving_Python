'''
Problem Solving Baekjoon 13460
Author: Injun Son
Date: September 17, 2020
'''
import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]
#빨간 구슬, 파란 구슬 2개가 동시에 움직이므로, 각 2개의 구슬 x, y좌표를 visited 배열에 4차원으로 선언하고 False로 초기화합니다.
visited = [[[[False]*m for _ in range(n)] for _ in range(m)] for _ in range(n)]
dx, dy = (-1, 0, 1, 0), (0, 1, 0, -1)
q = deque()

def init():
    ry, rx, by, bx = [0]*4 #초기화 0,0,0,0
    for i in range(n):
        for j in range(m):
            if board[i][j]=='R':
                ry, rx = i, j
            elif board[i][j]=='B':
                by, bx = i, j
    q.append((ry, rx, by, bx, 1)) #위치 정보와 depth
    visited[ry][rx][by][bx] = True

def move(y, x, dy, dx):
    count = 0 #이동한 칸 수
    #다음 이동이 벽이거나 구멍이 아닐 때까지
    while board[y+dy][x+dx] !='#' and board[y][x] !='O':
        y +=dy
        x +=dx
        count +=1
    return y, x, count

def bfs():
    init()
    while q:
        ry, rx, by, bx, depth = q.popleft()
        if depth > 10:
            break
        for i in range(len(dx)):
            nry, nrx, rcount = move(ry, rx, dy[i], dx[i])
            nby, nbx, bcount = move(by, bx, dy[i], dx[i])

            if board[nby][nbx] == 'O':
                continue
            if board[nry][nrx] == 'O':
                print(depth)
                return

            #빨간 구슬과 파란 구슬이 동시에 같은 칸에 있을 수 없다
            if nrx==nbx and nry==nby:
                if rcount > bcount: #이동 거리가 많은 구슬을 한칸 뒤로
                    nrx -= dx[i]
                    nry -= dy[i]
                else:
                    nbx -= dx[i]
                    nby -= dy[i]

            #bfs탐색을 마치고 방문 여부 확인
            if not visited[nry][nrx][nby][nbx]:
                visited[nry][nrx][nby][nbx] = True
                q.append((nry,nrx, nby, nbx, depth+1))

    print(-1) #실패

bfs()

