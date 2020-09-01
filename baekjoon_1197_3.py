'''
Problem Solving Baekjoon 1197_3
Author: Injun Son
Date: October 1, 2020
'''
import math, sys
import heapq

'''
크루스칼 알고리즘으로 풀기
'''

def Find(x):
    if p[x]==x:
        return x
    else:
        p[x] = Find(p[x])
        return p[x]

def Union(x, y):
    x = Find(x)
    y = Find(y)
    if x!=y:
        p[y]=x

V, E = map(int, sys.stdin.readline().split())
G = []
p = [i for i in range(V+1)]

for _ in range(E):
    A, B, C = map(int, sys.stdin.readline().split())
    G.append([C, A, B])

G.sort(key = lambda x: x[0])
E_count = 0
MST = 0
for i in range(E):
    dis = G[i][0]
    start = G[i][1]
    end = G[i][2]
    if Find(start) != Find(end):
        Union(start, end)
        MST += dis
        E_count +=1
    if E_count == V-1:
        break

print(MST)