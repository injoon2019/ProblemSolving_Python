'''
Problem Solving Baekjoon 16953
Author: Injun Son
Date: September 4, 2020
'''
from collections import deque
import sys
from itertools import combinations
SIZE = 10**9
def bfs(num):
    if num==B:
        return 1
    visited = dict()
    q = deque()
    q.append([num, 0])
    while q:
        num, cnt= q.popleft()
        if num == B:
            return cnt+1
        else:
            if num*2<=10**9+1 and num*2 not in visited:
                visited[num*2]=1
                q.append([num*2, cnt+1])
            ny = num*10 +1
            if ny<=10**9+1 and ny not in visited:
                visited[ny]=1
                q.append([ny, cnt+1])
    return -1

A, B = map(int, input().split())
print(bfs(A))