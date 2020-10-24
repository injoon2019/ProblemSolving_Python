'''
Problem Solving leetcode reconstruct-itinerary
Author: Injun Son
Date: October 24, 2020
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
    #그래프 순서대로 구성
    for a, b in sorted(tickets):
        graph[a].append(b)

    route = []
    def dfs(a):
        # 첫 번째 값을 읽어 어휘 순 방문
        while graph[a]:
            dfs(graph[a].pop(0))
        route.append(a)

    dfs('JFK')
    #다시 뒤집어 어휘 순 결과로
    return route[::-1]


print(findItinerary([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]))
# print(findItinerary([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]))
# print(findItinerary([["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]))