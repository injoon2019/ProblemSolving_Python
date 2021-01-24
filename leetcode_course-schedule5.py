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
    for x, y in prerequisites:
        graph[x].append(y)

    traced = set()
    visited = set()

    def dfs(i):
        # 순환 구조이면 False
        if i in traced:
            return False
        # 이미 방문했던 노드이면 True
        if i in visited: # 만약 순환 노드였으면 진작 걸러졌을 것이다. 남아 있는 것은 순환이 아닌 노드이므로 True
            return True

        traced.add(i)
        for y in graph[i]:
            if not dfs(y):
                return False
            # 탐색 종료 후 순환 노드 삭제
        traced.remove(i)
        visited.add(i)

        return True

    for x in list(graph):
        if not dfs(x):
            return False

    return True

# print(canFinish(2, [[1,0]]))
print(canFinish(2, [[0,1], [0,2], [1,2]]))