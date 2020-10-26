'''
Problem Solving leetcode course-schedule2
Author: Injun Son
Date: October 26, 2020
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


def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool:
    graph = collections.defaultdict(list)
    for a, b in prerequisites:
        graph[a].append(b)

    traced = set()
    visited = set()
    def dfs(i):
        if i in traced:
            return False

        if i in visited:
            return True

        traced.add(i)
        for y in graph[i]:
            if not dfs(y):
                return False

        traced.remove(i)
        visited.add(i)
        return True

    for x in list(graph):
        if not dfs(x):
            return False
    return True

print(canFinish(2, [[1,0]]))
print(canFinish(2, [[1,0], [0,1]]))