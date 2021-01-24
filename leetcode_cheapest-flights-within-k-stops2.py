'''
Problem Solving leetcode cheapest-flights-within-k-stops
Author: Injun Son
Date: January 24, 2020
'''
import heapq
import sys
import collections
from typing import List
from collections import defaultdict
sys.setrecursionlimit(100000)
import re
from collections import deque


def findCheapestPrice(n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
    graph = collections.defaultdict(list)
    for u, v, w in flights:
        graph[u].append((v, w))

    Q = [(0, src, K)]

    while Q:
        price, node, k = heapq.heappop(Q)
        if node == dst:
            return price
        if k >= 0:
            for v, w in graph[node]:
                alt = price + w
                heapq.heappush(Q, (alt, v, k-1))
    return -1

# print(findCheapestPrice(3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 1))
# print(findCheapestPrice(5, [[1,2,10],[2,0,7],[1,3,8],[4,0,10],[3,4,2],[4,2,10],[0,3,3],[3,1,6],[2,4,5]], 0, 4, 1))
# print(findCheapestPrice(5, [[4,1,1],[1,2,3],[0,3,2],[0,4,10],[3,1,1],[1,4,3]], 2, 1, 1))
print(findCheapestPrice(4, [[0,1,1],[0,2,5],[1,2,1],[2,3,1]], 0, 3, 1))