'''
Problem Solving leetcode kth-largest-element-in-an-array
Author: Injun Son
Date: January 1, 2020
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


def findKthLargest(nums: List[int], k: int) -> int:
    heap = list()
    for n in nums:
        heapq.heappush(heap, -n)

    for _ in range(k):
        heapq.heappop(heap)

    return -heapq.heappop(heap)


# def findKthLargest(nums: List[int], k: int) -> int:
#     heapq.heapify(nums)
#
#     for _ in range(len(nums) - k):
#         heapq.heappop(nums)
#
#     return heapq.heappop(nums)

def findKthLargest(self, nums: List[int], k: int) -> int:
    return heapq.nlargest(k, nums)[-1]


print(findKthLargest([3, 2, 1, 5, 6, 4], 2))
print(findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))
