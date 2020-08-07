'''
Problem Solving Baekjoon 1167
Author: Injun Son
Date: August 7, 2020
'''
#https://pacific-ocean.tistory.com/324
from heapq import heappush, heappop
import sys
INF = sys.maxsize

def dijkstra(start):
        heap = []
        heappush(heap, [0, start]) #다익스트라 시작점 [weight, startPoint]
        d = [INF for i in range(n+1)] #start의 인접노드들까지의 거리를 일단 전부 INF 로 설정
        d[start] = 0
        while heap:
            weight, node = heappop(heap)
            for node_number, node_weight in s[node]: #node의 인접노드들에 대해 weight 갱신
                new_weight = node_weight + weight
                if d[node_number] > new_weight:
                    d[node_number] = new_weight
                    heappush(heap, [new_weight, node_number])
        return d

n = int(input())
s = [[] for i in range(n+1)]
for i in range(1, n+1):
    a = list(map(int, input().split()))
    for j in range(1, len(a), 2):
        if a[j] != -1:
            s[a[0]].append([a[j], a[j+1]])

print(s)
di = dijkstra(1)
print(max(dijkstra(di.index(max(di[1:])))[1:]))