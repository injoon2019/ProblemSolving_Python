'''
Problem Solving leetcode product_of_array_except_self
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

def productExceptSelf(nums: List[int]) -> List[int]:

    p = 1
    left = []
    for i in range(len(nums)):
        left.append(p)
        p *= nums[i]

    right = []
    p =1
    for i in range(len(nums)-1, -1, -1):
        right.append(p)
        p *= nums[i]

    right = right[::-1]
    out = []
    for i in range(len(left)):
        out.append(left[i]*right[i])

    return out

print(productExceptSelf([1,2,3,4]))

