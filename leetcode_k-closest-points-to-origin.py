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
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        return sorted(points, key = lambda x: (x[0]-0)**2 + (x[1]-0)**2)[:K]

sol = Solution()
print(sol.kClosest([[1,3],[-2,2]], 1))