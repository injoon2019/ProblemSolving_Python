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
    result = []

    def dfs(elements, count, cur_num):
        if count == k:
            result.append(elements[:])
            return

        for i in range(cur_num, n+1):
            elements.append(i)
            dfs(elements, count + 1, i+1)
            elements.pop()

    dfs([], 0, 1)
    return result


print(combine(4, 2))
