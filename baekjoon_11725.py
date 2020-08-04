'''
Problem Solving Baekjoon 11725
Author: Injun Son
Date: August 3, 2020
'''
import sys
N = int(sys.stdin.readline())
tree = [[] for _ in range(N+1)]
for _ in range(N-1):
    s, e = map(int, sys.stdin.readline().split())
    tree[s].append(e)
    tree[e].append(s)

#부모저장
parents = [0 for _ in range(N+1)]

def DFS(start, tree, parents):
    for i in tree[start]: #연결된 노드 모두 탐색
        if parents[i]==0: #한번도 방문 안했다면
            parents[i]=start
            DFS(i, tree, parents)

DFS(1, tree, parents)

for i in range(2, N+1):
    print(parents[i])