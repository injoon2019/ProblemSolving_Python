'''
Problem Solving leetcode reconstruct-itinerary
Author: Injun Son
Date: January 24, 2021
'''
import sys
import collections
import heapq
import functools
import itertools
import re
import math
import bisect
from typing import *


def findItinerary(tickets: List[List[str]]) -> List[str]:
    graph = collections.defaultdict(list)
    # 그래프 순서대로 구성
    for a, b in sorted(tickets, reverse = True):
        graph[a].append(b)

    print(graph)
    route = []
    def dfs(a):
        # 첫 번째 값을 읽어 어휘 순 방문
        print(a, route)
        while graph[a]:
            dfs(graph[a].pop())
        route.append(a)

    dfs('JFK')
    return route[::-1]

# print(findItinerary([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]))
# print(findItinerary([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]))
print(findItinerary([["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]))