'''
Problem Solving Baekjoon 1525_2
Author: Injun Son
Date: August 19, 2020
'''
from collections import deque
import sys

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

dist = dict()
aa = ''

def bfs():
    q = deque()
    q.append(aa)
    dist[aa] = 0

    while q:
        d = q.popleft()
        if d==123456789:
            return dist[d]

        s = str(d)
        k = s.find('9')
        x, y = k//3, k%3

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0 <=nx<3 and 0<=ny<3:
                nk = nx*3+ny #새 좌표 위치
                ns = list(s)
                ns[k], ns[nk] = ns[nk], ns[k]
                nd = int(''.join(ns))

                if not dist.get(nd):
                    dist[nd] = dist[d]+1
                    q.append(nd)
    return -1

for _ in range(3):
    a = input()
    a= a.replace(" ", "")
    aa+=a

#0대신 9사용
aa = int(aa.replace('0', '9'))
print(bfs())
