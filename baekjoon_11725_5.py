'''
Problem Solving Baekjoon 11725_5
Author: Injun Son
Date: January 8, 2020
'''
import sys

N = int(input())
tree = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

parents = [0] * (N+1)  # i의 부모는 parents[i]이다

def DFS(start, tree, parents):
    for i in tree[start]:
        if parents[i] == 0:
            parents[i] = start
            DFS(i, tree, parents)

DFS(1, tree, parents)

for i in range(2, N+1):
    print(parents[i])