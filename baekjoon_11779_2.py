'''
Problem Solving Baekjoon 11779_2
Author: Injun Son
Date: September 1, 2020
'''
import sys
import heapq
MAX = sys.maxsize
#도시의 개수
N = int(input())
#버스의 개수
M = int(input())
graph = [ [] for _ in range(N+1)]
path = [100001]*(N+1)

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])

def dijkstra(start):
    d = [MAX]*(N+1)
    d[start]=0
    heap = []
    heapq.heappush(heap, start)
    path[start] = start
    while heap:
        v = heapq.heappop(heap)
        for adj_node, cost in graph[v]:
            if d[adj_node] > d[v]+cost:
                d[adj_node] = d[v] + cost
                heapq.heappush(heap, adj_node)
                path[adj_node] = v
    return d

start_city, end_city = map(int, input().split())
d = dijkstra(start_city)
print(d[end_city])
ans = [end_city]
while end_city != start_city:
    ans.append(path[end_city])
    end_city = path[end_city]

print(len(ans))
for i in range(len(ans)-1, -1, -1):
    print(ans[i], end=" ")