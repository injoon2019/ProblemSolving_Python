'''
Problem Solving leetcode subsets
Author: Injun Son
Date: October 23, 2020
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

    def dfs(index, path):
        result.append(path)

        for i in range(index, len(nums)):
            dfs(i+1, path+[nums[i]])

    dfs(0, [])
    return result

print(subsets([1,2,3]))