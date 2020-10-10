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
    anagrams = collections.defaultdict(list)

    for word in strs:
        anagrams[''.join(sorted(word))].append(word)

    return anagrams.values()

print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))

