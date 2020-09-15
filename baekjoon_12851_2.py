'''
Problem Solving Baekjoon 12851_2
Author: Injun Son
Date: September 15, 2020
'''
from collections import deque
import heapq
import sys, copy

n, k = map(int, input().split())
#ch[i][0]는 i까지 도달하는 가장 빠른 시간, ch[i][1]은 방법의 수
ch = [[-1,0] for _ in range(100001)]

def bfs(n):
    q = deque()
    q.append(n)
    ch[n][0] = 0
    ch[n][1] = 1

    while q:
        x = q.popleft()
        for i in (x+1, x-1, x*2):
            if 0<= i <100001:
                #처음 들르는 경우
                if ch[i][0]==-1:
                    ch[i][0] = ch[x][0]+1
                    ch[i][1] = ch[x][1]
                    q.append(i)
                #한번 이상 들리는 경우
                elif ch[i][0] == ch[x][0]+1:
                    ch[i][1] += ch[x][1]

bfs(n)
print(ch[k][0])
print(ch[k][1])