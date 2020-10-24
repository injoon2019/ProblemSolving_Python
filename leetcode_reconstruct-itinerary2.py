'''
Problem Solving leetcode reconstruct-itinerary2
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
    for a, b in sorted(tickets):
        graph[a].append(b)

    route = []
    def dfs(a):
        print(a)
        while graph[a]:
            dfs(graph[a].pop(0))
        route.append(a)

    dfs('JFK')
    return route[::-1]

# print(findItinerary([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]))
# print(findItinerary([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]))
print(findItinerary([["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]))