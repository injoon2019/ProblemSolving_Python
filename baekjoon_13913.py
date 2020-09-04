'''
Problem Solving Baekjoon 13913
Author: Injun Son
Date: September 3, 2020
'''
import sys
from collections import deque
sys.setrecursionlimit(100000)
MAX = 100001

def solve(visited, n, k):
    queue = deque()
    queue.append(n)
    while queue:
        x = queue.popleft()

        if x==k:
            print(visited[x])
            #역추적
            p = []
            while x != n:
                p.append(x)
                x = path[x]
            p.append(n)
            for i in range(len(p)-1, -1, -1):
                print(p[i], end= " ")
            return

        for nx in (x+1, x-1, x*2):
            if 0<=nx<100001 and visited[nx]==0:
                visited[nx] = visited[x]+1
                #path[다음좌표]=현재좌표 나중에 역추적
                path[nx] = x
                queue.append(nx)

n, k = map(int, input().split())
visited =  [0]*100001
path = [0]*100001
solve(visited, n, k)