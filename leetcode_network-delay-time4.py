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
    graph = collections.defaultdict()
    # 그래프 인접리스트 구성
    for u, v, w in times:
        graph[u].append((v,w))

    Q = [(0, K)] # (time, adj_node)
    dist = collections.defaultdict(int)

    while Q:
        node, time = heapq.heappop(Q)
        if node not in dist:
            dist[node] = time
            for v, w in graph[node]:
                alt = time + v
                heapq.heappush(Q, (alt, v))

    if len(dist) == N:
        return max(dist.values())
    return -1



networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], 4, 2)