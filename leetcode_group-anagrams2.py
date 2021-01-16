'''
Problem Solving leetcode group-anagrams
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

def groupAnagrams(strs: List[str])-> List[List[str]]:
    dict = collections.defaultdict(list)
    for word in strs:
        dict[''.join(sorted(word))].append(word)
    return dict.values()
print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))

