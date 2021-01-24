'''
Problem Solving leetcode combination-sum
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


def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
    result = []

    def dfs(elements, cur_index):
        if sum(elements) > target:
            return

        if sum(elements) == target:
            result.append(elements[:])

        for i in range(cur_index, len(candidates)):
            elements.append(candidates[i])
            dfs(elements, i)
            elements.pop()

    dfs([], 0)
    return result

print(combinationSum([2,3,6,7], 7))