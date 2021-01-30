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
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid -1
            elif nums[mid] < target:
                low = mid + 1
        return -1

sol = Solution()
print(sol.search( [-1,0,3,5,9,12], 9))