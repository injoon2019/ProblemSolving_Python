'''
Problem Solving leetcode course-schedule2
Author: Injun Son
Date: October 25, 2020
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
    # 그래프 구성
    for x, y in prerequisites:
        graph[x].append(y)

    traced = set()
    visited = set()

    def dfs(i):
        # 순환 구조이면 False
        if i in traced:
            return False
        # 이미 방문 했던 노드이면 True
        if i in visited:
            return True

        traced.add(i)
        for y in graph[i]:
            if not dfs(y):
                return False

        #탐색 종료 후 순환 노드 삭제
        traced.remove(i)
        #탐색 종료 후 방문 노드 추가
        visited.add(i)

        return True

    for x in list(graph):
        if not dfs(x):
            return False
    return True
print(canFinish(2, [[1,0]]))
print(canFinish(2, [[1,0], [0,1]]))