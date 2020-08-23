'''
Problem Solving Baekjoon 3108
Author: Injun Son
Date: August 23, 2020
'''
from collections import deque
import sys
'''
예제 입력처럼 접점이 없는 사격형이 있지만 좌표상으로는 한 칸차이라서 
bfs로 이동가능한 케이스가 존재한다
따라서 사각형의 모든 길이를 2배하면 간단하게 해결할 수 있다

1. 문제 입력이 -500~500 때문에 0~2000 으로 수정한 리스트를 만든다
2. 입력 좌표에 500을 더하고 2를 곱한다
3. start 리스트에 x1, y1 좌표를 저장하여 bfs 시작 좌표로 사용한다
4. 지도가 되는 리스트 a에 사각형의 변을 1로 표시해준다
5. start안의 좌표를 하나씩 꺼내와서 방문한 적이 없으면 bfs를 실행하고 ans를 증가시킨다
6. 연필을 내린 상태로 시작하기 때문에 만일 입력에 원점이 존재할 경우 ans에 1을 뺀 후 출력한다
'''

input = sys.stdin.readline
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
    q.append([x, y])
    c[x][y] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx <= 2000 and 0 <= ny <= 2000:
                if a[nx][ny] == 1 and c[nx][ny] == 0:
                    c[nx][ny] = 1
                    q.append([nx, ny])


n = int(input())
a = [[0]*2001 for _ in range(2001)]
c = [[0]*2001 for _ in range(2001)]
start = []
for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    x1 += 500; y1 += 500; x2 += 500; y2 += 500
    x1 *= 2; y1 *= 2; x2 *= 2; y2 *= 2
    start.append([x1, y1])
    for i in range(x1, x2+1):
        if i == x1 or i == x2:
            for j in range(y1, y2+1):
                a[i][j] = 1
        else:
            a[i][y1] = 1
            a[i][y2] = 1

q = deque()
ans = 0
for i in range(len(start)):
    x, y = start[i]
    if c[x][y] == 0:
        bfs(x, y)
        ans += 1

if a[1000][1000] == 1:
    ans -= 1
print(ans)