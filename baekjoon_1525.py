'''
Problem Solving Baekjoon 1525
Author: Injun Son
Date: August 19, 2020
'''
from collections import deque
import sys
def bfs():
    de = deque()
    de.append(aa)
    dist[aa] = 0

    while de:
        d = de.popleft()
        if d ==123456789:
            return dist[d]

        s = str(d)
        k = s.find('9')
        x, y = k//3, k%3  #3X3표일 때, x, y좌표

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0<=nx<3 and 0<=ny <3:
                nk = nx*3 + ny #3X3표에서 x,y좌표를 바꿨을때의 위치
                ns = list(s)
                ns[k], ns[nk] = ns[nk], ns[k]
                nd = int(''.join(ns))

                if not dist.get(nd):
                    dist[nd] = dist[d] +1
                    de.append(nd)
    return -1


dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

dist = dict()
aa = ''

for i in range(3):
    a = input()
    a=a.replace(' ', '')
    aa +=a

#0대신 9를 사용할거다
aa = int(aa.replace('0', '9'))
print(bfs())

