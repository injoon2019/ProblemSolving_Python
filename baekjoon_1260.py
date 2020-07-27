'''
Problem Solving Baekjoon 1260
Author: Injun Son
Date: July 27, 2020
'''
queue = []
stack = []
def DFS(V):
    global arr, check
    if check[V] == True:
        return

    print(V, end=" ")
    check[V]=True
    for i in arr[V]:
        DFS(i)

def BFS(V):
    global arr, check
    queue.append(V)
    check[V]=True
    while queue:
        v = queue.pop(0)
        print(v, end=" ")
        for i in arr[v]:
            if check[i]==False:
                check[i]=True
                queue.append(i)


N, M, V = map(int, input().split())
arr = [[] for r in range(N+1)]
check = [False]*(N+1)
for _ in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

for i in arr:
    i.sort()
DFS(V)
print()
check = [False]*(N+1)
BFS(V)
