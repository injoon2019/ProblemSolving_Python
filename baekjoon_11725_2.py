'''
Problem Solving Baekjoon 11725_2
Author: Injun Son
Date: August 3, 2020
'''
import sys
N = int(sys.stdin.readline())
tree = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    tree[a].append(b)
    tree[b].append(a)

parents = [0 for _ in range(N+1)]


def dfs(start):
    for i in tree[start]:
        if parents[i]==0:
            parents[i] = start
            dfs(i)

dfs(1)

for i in range(2, N+1):
    print(parents[i])