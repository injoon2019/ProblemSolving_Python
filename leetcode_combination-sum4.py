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

    def dfs(csum, index, path):
        if csum < 0:
            return
        if csum == 0:
            result.append(path)
            return

        for i in range(index, len(candidates)):
            dfs(csum - candidates[i], i, path + [candidates[i]])

    dfs(target, 0, [])
    return result


print(combinationSum([2,3,6,7], 7))