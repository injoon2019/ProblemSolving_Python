'''
Problem Solving leetcode permutations
Author: Injun Son
Date: October 23, 2020
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

def permute(nums: List[int]) -> List[List[int]]:
    return list(itertools.permutations(nums, len(nums)))
print(permute([1,2,3]))
print(permute([1]))