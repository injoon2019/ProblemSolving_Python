'''
Problem Solving leetcode permutations
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

def permute(nums: List[int]) -> List[List[int]]:
    results = []
    prev_elements = []

    def dfs(elements):
        if len(elements) == 0:
            results.append(prev_elements[:])

        for e in elements:
            next_elements = elements[:]
            next_elements.remove(e)

            prev_elements.append(e)
            dfs(next_elements)
            prev_elements.pop()

    dfs(nums)
    return results


print(permute([1,2,3]))
# print(permute([1]))