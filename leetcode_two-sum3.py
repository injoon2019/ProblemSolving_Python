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
    num_maps = {}
    for i, num in enumerate(nums):
        if target - num in num_maps:
            return [num_maps[target - num], i]
        num_maps[num] = i

print(twoSum([2,7,11,15], 9))