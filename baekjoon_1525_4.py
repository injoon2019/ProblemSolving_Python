'''
Problem Solving Baekjoon 1525_3
Author: Injun Son
Date: September 16, 2020
'''
from collections import deque
import sys

dx = [-1, 0, 0, 1]
dy = [0, 1, -1, 0]

aa = ''
dist = dict()

def bfs():
    q = deque()
    dist[aa] = 0
    q.append(aa)

    while q:
        d = q.popleft()
        if d == 123456789:
            return dist[d]

        else:
            empty_ind = str(d).find('9')
            y, x = empty_ind//3, empty_ind%3
            for i in range(4):
                ny, nx = y+dy[i], x+dx[i]
                if 0<=nx<3 and 0<=ny<3:
                    ns = list(str(d))
                    ns[y*3+x], ns[ny*3+nx] = ns[ny*3+nx], ns[y*3+x]
                    ns = int(''.join(ns))

                if ns not in dist.keys():
                    q.append(ns)
                    dist[ns] = dist[d]+1
    return -1


for _ in range(3):
    a = input()
    a = a.replace(' ', '')
    aa += a

aa = int(aa.replace('0', '9'))
print(bfs())
