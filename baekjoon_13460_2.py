'''
Problem Solving Baekjoon 13460_2
Author: Injun Son
Date: September 17, 2020
'''
import sys
from collections import deque

input = sys.stdin.readline
r, c = map(int, input().split())
board = [list(input()) for _ in range(r)]

#빨간 구슬의 y,x 좌표, 파란 구슬의 y,x 좌표 한번에 관리 해줘야한다
visited = [[[[False]*c for _ in range(r)] for _ in range(c)] for _ in range(r)]
dx, dy = (-1, 0, 0, 1), (0, 1, -1, 0)
q = deque()

def init():
    ry,rx, by, bx = [0]*4 #초기화 0,0,0,0
    for i in range(r):
        for j in range(c):
            if board[i][j]=='R':
                ry, rx = i, j
            elif board[i][j]=='B':
                by, bx = i, j
    q.append((ry, rx, by, bx, 1)) #위치 정보와 depth
    visited[ry][rx][by][bx] = True

def move(y, x, dy, dx):
    count = 0 #이동한 칸의 수
    #그냥 일단 R, B가 겹쳐도 벽이 아닌이상 이동할 수 있는만큼 끝까지 이동시키는게 편하다
    while board[y+dy][x+dx] !='#' and board[y][x] !='O':
        y += dy
        x += dx
        count +=1
    return y, x, count

def bfs():
    init()
    while q:
        ry, rx, by, bx, depth = q.popleft()
        if depth > 10:
            break
        for i in range(4):
            #나는 처음 문제 풀때, 같은 row에 있으면 왼쪽에 있는 것은 먼저 왼쪽으로 굴려줘야한다고 생각했다.
            #하지만 편하게 문제를 푸는 방법은 일단 순서에 상관없이 둘 다 굴리고, 둘이 겹치면 원래 왼쪽에 있던 것을
            #다시 한칸 옮기면 그만이다.
            nry, nrx, rcount = move(ry, rx, dy[i], dx[i])
            nby, nbx, bcount = move(by, bx, dy[i], dx[i])

            #파란거는 빠지면 안된다
            if board[nby][nbx]=='O':
                continue
            if board[nry][nrx] == 'O':
                print(depth)
                return

            #빨간 구슬과 파란 구슬이 동시에 같은 칸에 있을 수 없다
            if nrx==nbx and nry==nby:
                if rcount > bcount:
                    nrx -= dx[i]
                    nry -= dy[i]
                else:
                    nbx -= dx[i]
                    nby -= dy[i]

            #bfs 탐색을 마치고 방문 여부를 확인
            if not visited[nry][nrx][nby][nbx]:
                visited[nry][nrx][nby][nbx] = True
                q.append((nry, nrx, nby, nbx, depth+1))

    print(-1)
bfs()