'''
Problem Solving Baekjoon 17141_2
Author: Injun Son
Date: September 18, 2020
'''
'''
잘 풀었지만, 시간 단축과 itertools 대신 백트랙킹으로 푸는 것 연습을 위해
https://rebas.kr/845 에서 참고함 
'''
from collections import deque

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
select = [False]*10
q, v, k = deque(), [], 0 #v는 virus 가능 위치 저장

def bfs(dist):
    global ans
    infect, times = 0, 0
    while q:
        y, x = q.popleft()
        times = dist[y][x]
        for dy, dx in (-1,0), (1,0), (0,1), (0,-1):
            ny, nx = y+dy, x+dx
            if nx<0 or nx>=n or ny<0 or ny>=n:
                continue
            #원본 그래프에서 벽이 아니고, 처음 방문하는 곳이라면
            if a[ny][nx] != 1 and dist[ny][nx]== -1:
                dist[ny][nx] = dist[y][x]+1
                q.append((ny, nx))
                infect +=1

    if infect==k:
        ans = min(ans, times)

def solve(idx, cnt, d):
    if cnt ==m:
        dist = [[-1]*n for _ in range(n)]
        for i in range(d):
            if select[i]: # 바이러스 위치가 선택되었다면
                y, x = v[i]
                q.append((y, x))
                dist[y][x] = 0 #바이러스 있는 곳 0으로 만든다
        bfs(dist)
        return

    for i in range(idx, d):
        if not select[i]:
            select[i] = True
            solve(i+1, cnt+1, d)
            select[i] = False

for i in range(n):
    for j in range(n):
        if a[i][j] ==2: #virus 놓을 수 있는 위치 저장
            v.append((i,j))
        if a[i][j] == 0: #빈칸의 개수 세기
            k +=1

ans = 10**9
k = k+ len(v) -m #바이러스 설치 할 수 있는 곳에서 실제 설치할 m개 를 뺸 것도 빈칸 개수에 더해준다
solve(0, 0, len(v))
print(ans if ans != 10**9 else -1)