'''
Problem Solving leetcode binary-search
Author: Injun Son
Date: January 30, 2021
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

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        index = bisect.bisect_left(nums, target)

        if index < len(nums) and nums[index] == target:
            return index

        else:
            return -1



sol = Solution()
print(sol.search( [-1,0,3,5,9,12], 9))