'''
Problem Solving Baekjoon 16927
Author: Injun Son
Date: September 15, 2020
'''
from collections import deque
import heapq
import sys, copy

n, m, r = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
k = min(n, m)//2

for o in range(k):
    group = []
    for j in range(o, m-o):
        group.append(a[o][j])
    for i in range(o+1, n-o):
        group.append(a[i][m-o-1])
    for j in range(m-o-2, o-1,-1):
        group.append(a[n-o-1][j])
    for i in range(n-o-2, 0, -1):
        group.append(a[i][o])

    l = r%len(group)
    group = group[l:]+group[:l]
    group = group[::-1]
    for j in range(o,m-o):
        a[o][j] = group.pop()
    for i in range(o+1,n-o):
        a[i][m-o-1] = group.pop()
    for j in range(m-o-2,o-1,-1):
        a[n-o-1][j] = group.pop()
    for i in range(n-o-2,o,-1):
        a[i][o] = group.pop()

for row in range(n):
    print(' '.join(map(str, a[row])))

