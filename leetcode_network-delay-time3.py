'''
Problem Solving leetcode network-delay-time
Author: Injun Son
Date: October 28, 2020
'''
import sys
import collections
import heapq
import functools
import itertools
import re
import math
import bisect
from collections import deque
from typing import *


def networkDelayTime(times: List[List[int]], N: int, K: int) -> int:
    graph = [[] for _ in range(N+1)]
    for time in times:
        u, v, w = time
        graph[u].append([v, w])

    def dijkstra(K):
        d = [sys.maxsize] * (N+1)
        d[K]=0
        queue = deque()
        queue.append([K, 0])
        while queue:
            node, cost = queue.popleft()
            for adj_node in graph[node]:
                if d[adj_node[0]] > cost + adj_node[1]:
                    d[adj_node[0]] = cost + adj_node[1]
                    queue.append([adj_node[0], cost + adj_node[1]])

        return d[1:]

    distanc_list = dijkstra(K)

    if max(distanc_list) == sys.maxsize:
        return -1
    else:
        return max(distanc_list)
networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], 4, 2)