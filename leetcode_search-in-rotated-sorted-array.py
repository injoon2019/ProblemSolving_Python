'''
Problem Solving leetcode search-in-rotated-sorted-array
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
        return nums.index(target) if target in nums else -1

sol = Solution()
print(sol.search( [4,5,6,7,0,1,2], 0))