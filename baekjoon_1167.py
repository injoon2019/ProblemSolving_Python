'''
Problem Solving Baekjoon 1167
Author: Injun Son
Date: August 4, 2020
'''
#https://pacific-ocean.tistory.com/324
from heapq import heappush, heappop
import sys
INF = sys.maxsize
def dijkstra(start):
    pass

n = int(input())
s = [[] for i in range(n+1)]
for i in range(1, n+1):
    a = list(map(int, input().split()))
    for j in range(1, len(a), 2):
        if a[j] != -1:
            s[a[0]].append([a[j], a[j+1]])
print(s)