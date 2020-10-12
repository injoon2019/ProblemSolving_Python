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
    out = []
    p = 1
    # 왼쪽 곱셈
    for i in range(0, len(nums)):
        out.append(p)
        p = p * nums[i]
    p = 1
    #왼쪽 곱셈 결과에 오른쪽 값을 차례대로 곱셈
    for i in range(len(nums)-1, 0-1, -1):
        out[i] = out[i]*p
        p = p * nums[i]

    return out

print(productExceptSelf([1,2,3,4]))

