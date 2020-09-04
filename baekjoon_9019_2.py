'''
Problem Solving Baekjoon 9019_2
Author: Injun Son
Date: September 4, 2020
'''
from collections import deque
import sys
from collections import deque
input = sys.stdin.readline
def bfs(num):
    visited = [0]*10000
    dq = deque()
    dq.append([num, ''])
    visited[num] = 1
    while dq:
        v, cmd_list = dq.popleft()
        visited[v]=True
        if v == target:
            print(cmd_list)
            return
        else:
            if visited[(2*v)%10000]==0:
                dq.append([(2*v)%10000, cmd_list+'D'])

            if v-1>=0 and visited[v-1]==0:
                visited[v-1] =1
                dq.append([v-1, cmd_list+'S'])

            if v==0 and visited[9999]==0:
                visited[9999]=1
                dq.append([9999,  cmd_list + 'S'])

            nx = int((v%1000)*10+ v//1000)
            if visited[nx]==0:
                visited[nx]=1
                dq.append([nx, cmd_list+'L'])

            nx = int((v % 10) * 1000 + v / 10)
            if visited[nx] == 0:
                visited[nx] = 1
                dq.append([nx, cmd_list+'R'])


T = int(input())
for _ in range(T):
    num, target = map(int, input().split())
    min_cnt = sys.maxsize
    bfs(num)
