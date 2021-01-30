'''
Problem Solving leetcode intersection-of-two-arrays
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
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1).intersection(set(nums2)))

sol = Solution()
print(sol.intersection([1,2,2,1], [2,2]))