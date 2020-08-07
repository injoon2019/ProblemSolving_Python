'''
Problem Solving Baekjoon 1967
Author: Injun Son
Date: August 7, 2020
'''
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
                #print(node, node_number)
                new_weight = node_weight + weight
                if d[node_number] > new_weight:
                    d[node_number] = new_weight
                    heappush(heap, [new_weight, node_number])
        return d

n = int(input())
s = [[] for i in range(n+1)]
count = 0
while True:
    try:
        a = list(map(int, input().split()))
        s[a[0]].append([a[1], a[2]])
        s[a[1]].append([a[0], a[2]])
        count +=1
    except:
        break
di = dijkstra(1)
print(max(dijkstra(di.index(max(di[1:])))[1:]))