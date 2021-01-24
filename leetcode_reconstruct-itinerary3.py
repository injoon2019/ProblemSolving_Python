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
    result = []
    for ticket in tickets:
        graph[ticket[0]].append(ticket[1])

    for key in graph.items():
        graph[key[0]].sort()

    def dfs(graph, start_point, path):
        # print(start_point, path)
        if len(path) == len(tickets) :
            result.append(path[:] + [start_point])
            return result

        for dest in graph[start_point][:]:
            if len(result) > 0:
                break
            graph[start_point].remove(dest)
            dfs(graph, dest, path[:] + [start_point])
            graph[start_point].append(dest)

    dfs(graph, "JFK", [])
    return result[0]

# print(findItinerary([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]))
print(findItinerary([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]))
# print(findItinerary([["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]))