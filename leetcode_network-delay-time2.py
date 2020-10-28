'''
Problem Solving leetcode network-delay-time2
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
    graph = collections.defaultdict(list)
    #그래프 인접 리스트 구성
    for u, v, w in times:
        graph[u].append((v, w))

    # 큐 변수: [(소요시간, 정점)]
    Q = [(0, K)]
    dist = collections.defaultdict(int)

    #우선순위 큐 최솟값 기준으로 정점까지 최단 경로 삽입
    while Q:
        time, node = heapq.heappop(Q)
        if node not in dist:
            dist[node] = time
            for v, w in graph[node]:
                alt = time + w
                heapq.heappush(Q, (alt, v))

    # 모든 노드의 최단 경로 존재 여부 판별
    if len(dist) ==N:
        return max(dist.values())
    return -1


networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], 4, 2)