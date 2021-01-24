'''
Problem Solving leetcode subsets
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


def subsets(nums: List[int]) -> List[List[int]]:
    result = []

    def dfs(path, cur_index):
        if cur_index == len(nums):
            result.append(path[:])
            return

        dfs(path[:] , cur_index + 1)
        dfs(path[:] + [nums[cur_index]], cur_index + 1)

        return result

    dfs([], 0)
    return result

print(subsets([1,2,3]))