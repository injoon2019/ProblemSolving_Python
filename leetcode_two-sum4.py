'''
Problem Solving leetcode two-sum
Author: Injun Son
Date: January 18, 2021
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
    tuples = list(enumerate(nums))
    # print(tuples)
    tuples.sort(key = lambda x: x[1])
    left , right = 0, len(tuples)-1
    # print(tuples)
    while left < right:
        # print(left, right)
        if tuples[left][1] + tuples[right][1] == target:
            return [tuples[left][0], tuples[right][0]]

        if tuples[left][1] + tuples[right][1] < target:
            left +=1

        else:
            right -=1

# print(twoSum([2,7,11,15], 9))
print(twoSum([3,2,4], 6))