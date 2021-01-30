'''
Problem Solving leetcode largest-number
Author: Injun Son
Date: January 29, 2021
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
    def sortColors(self, nums: List[int]) -> None:
        mid = 1
        i, j = 0, 0
        k = len(nums)
        while j < k:
            if nums[j] < mid:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j += 1
            elif nums[j] > mid:
                k -= 1
                nums[k], nums[j] = nums[j], nums[k]
            else:
                j += 1