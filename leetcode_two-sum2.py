'''
Problem Solving leetcode two-sum
Author: Injun Son
Date: October 10, 2020
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

def twoSum(nums: List[int], target:int) -> List[int]:
    for i, n in enumerate(nums):
        if target - n in nums[i+1:]:
            return i, nums[i+1:].index(target - n) + i+1

print(twoSum([2,7,11,15], 9))