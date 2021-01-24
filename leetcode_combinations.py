'''
Problem Solving leetcode combinations
Author: Injun Son
Date: January 22, 2021
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

def combine(n: int, k: int) -> List[List[int]]:
    results = []

    def dfs(elements, start: int, k: int):
        if k == 0:
            results.append(elements[:])

        for i in range(start, n+1):
            elements.append(i)
            dfs(elements, i + 1, k-1)
            elements.pop()

    dfs([], 1, k)
    return results

print(combine(4, 2))