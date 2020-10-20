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
    freqs_heap = []
    for f in freqs:
        heapq.heappush(freqs_heap, (-freqs[f], f))

    topk = list()
    for _ in range(k):
        topk.append(heapq.heappop(freqs_heap)[1])

    return topk

print(topKFrequent([1,1,1,2,2,3], 2))