'''
Problem Solving Baekjoon 2606
Author: Injun Son
Date: August 26, 2020
'''
import math, sys

N = int(input())
graph = [[] for i in range(N+1)]
edge_num = int(input())
for _ in range(edge_num):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

check_list = [False]*(N+1)
def dfs(v):
    check_list[v]=True
    for node in graph[v]:
        if check_list[node]==False:
            dfs(node)

dfs(1)
ans = 0
for i in check_list:
    if i==True:
        ans +=1

print(ans-1)