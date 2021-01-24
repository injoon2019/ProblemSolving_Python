'''
Problem Solving leetcode combinations
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

import itertools

def combine(n: int, k: int) -> List[List[int]]:
    return list(itertools.combinations(range(1, n + 1), k))c

print(combine(4, 2))