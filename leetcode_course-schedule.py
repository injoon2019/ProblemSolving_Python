'''
Problem Solving leetcode course-schedule
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
    for x, y in prerequisites:
        graph[x].append(y)

    traced = set()

    def dfs(i):
        #순환 구조이면 False
        if i in traced:
            return False

        traced.add(i)
        for y in graph[i]:
            if not dfs(y):
                return False
        # 탐색 종료 후 순환 노드 삭제
        traced.remove(i)

        return True

    #순환 구조 판별
    for x in list(graph):
        if not dfs(x):
            return False
    return True
print(canFinish(2, [[1,0]]))
print(canFinish(2, [[1,0], [0,1]]))