'''
Problem Solving Baekjoon 11779
Author: Injun Son
Date: September 1, 2020
'''
import sys
import heapq

n = int(input())
m = int(input())

distance = [sys.maxsize]*(n+1)
p = [100001]*(n+1)
edge = [[] for i in range(n+1)]
for i in range(m):
    s, e, w = map(int, input().split())
    edge[s].append([e, w])

start, target = map(int, input().split())
distance[start]=0
p[start] = start
heap = []
heapq.heappush(heap, (0, start))

while heap:
    wei, s = heapq.heappop(heap)
    if distance[s] < wei:
        continue
    for i in range(len(edge[s])):
        [e, w] = edge[s][i]
        if distance[e] > distance[s]+w:
            distance[e] = distance[s]+w
            heapq.heappush(heap, (distance[e], e))
            p[e] = s

print(distance[target])
ans = [target]
while start != target:
    ans.append(p[target])
    target = p[target]

print(len(ans))
for i in range(len(ans)-1, -1, -1):
    print(ans[i], end= " ")
