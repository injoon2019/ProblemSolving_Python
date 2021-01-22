'''
Problem Solving leetcode top-k-frequent-elements
Author: Injun Son
Date: October 20, 2020
'''
import heapq
import sys
import collections
from typing import List
from collections import defaultdict
sys.setrecursionlimit(100000)
import re

def topKFrequent(nums: List[int], k: int) -> List[int]:
    freqs = collections.Counter(nums)
    freq_list = sorted(freqs.items(), key = lambda x: (-x[1]))
    return list(x[0] for x in freq_list[:k])

print(topKFrequent([1,1,1,2,2,3], 2))
print(topKFrequent([4,1,-1,2,-1,2,3], 2))