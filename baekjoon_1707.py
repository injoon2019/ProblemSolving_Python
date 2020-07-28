'''
Problem Solving Baekjoon 1707
Author: Injun Son
Date: July 27, 2020
'''
import sys
sys.setrecursionlimit(100000)

K  = int(sys.stdin.readline())
flag = True
def dfs(v):
    global flag
    for i in arr[v]:
        if visited[i] == visited[v]:
            flag = False
            return
        elif visited[i] == 0:
            visited[i] = (-1)*visited[v]
            dfs(i)

for _ in range(K):
    V, E = map(int, sys.stdin.readline().rstrip().split())
    flag = True
    arr = [[] for _ in range(V+1)]
    visited = [0] * (V+1)
    for _ in range(E):
        a, b = map(int, sys.stdin.readline().rstrip().split())
        arr[a].append(b)
        arr[b].append(a)

    for i in range(1, V+1):
        if flag == False:
            break;
        if visited[i] == 0:
            visited[i] = 1
            dfs(i)

    if flag:
        print("YES")
    else:
        print("NO")


