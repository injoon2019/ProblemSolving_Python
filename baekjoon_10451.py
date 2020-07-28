'''
Problem Solving Baekjoon 10451
Author: Injun Son
Date: July 27, 2020
'''
import sys
sys.setrecursionlimit(100000)

T = int(sys.stdin.readline())
for _ in range(T):
    V = int(sys.stdin.readline())
    graph = list(map(int, sys.stdin.readline().rstrip().split()))
    graph = [0]+graph
    visited = [0]*(V+1)
    count = 0
    for i in range(1, V+1):
        if visited[i]==0:
            count+=1
            v = i
            while visited[v]==0:
                visited[v] = 1
                v = graph[v]

    print(count)
