'''
Problem Solving leetcode minimum-height-trees
Author: Injun Son
Date: November 11, 2020
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


def findMinHeightTrees(n: int, edges: List[List[int]]) -> List[int]:
    if n<=1:
        return [0]

    # 양방향 그래프 구성
    graph = collections.defaultdict(list)
    for i, j in edges:
        graph[i].append(j)
        graph[j].append(i)

    # 첫 번째 리프 노드 추가
    leaves = []
    for i in range(n+1):
        if len(graph[i]) == 1:
            leaves.append(i)

    # 루트 노드만 남을 때까지 반복 제거
    while n > 2:
        n -= len(leaves)
        new_leaves = []
        for leaf in leaves:
            neighbor = graph[leaf].pop()
            graph[neighbor].remove(leaf)

            if len(graph[neighbor]) == 1:
                new_leaves.append(neighbor)
            leaves = new_leaves
    return leaves