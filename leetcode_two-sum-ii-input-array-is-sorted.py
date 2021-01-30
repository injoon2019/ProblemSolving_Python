'''
Problem Solving leetcode two-sum-ii-input-array-is-sorted
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
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while (left <= right):
            if numbers[left] + numbers[right] == target:
                return [left+1, right+1]
            elif numbers[left] + numbers[right] < target:
                left += 1
            elif numbers[left] + numbers[right] > target:
                right -= 1


sol = Solution()
print(sol.intersection([2,7,11,15], 9))