'''
Problem Solving leetcode array_partition_i
Author: Injun Son
Date: October 11, 2020
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

def arrayPairSum(nums: List[int]) -> int:
    nums.sort()
    total = 0
    for i in range(0, len(nums), 2):
        total += nums[i]
    return total

print(arrayPairSum([1,4,3,2]))

