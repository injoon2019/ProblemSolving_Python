'''
Problem Solving leetcode trapping-rain-water
Author: Injun Son
Date: January 17, 2020
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


def trap(height: List[int]) -> int:
    stack = []
    total = 0

    for i in range(len(height)):
        while stack and height[i] > height[stack[-1]]:
            top = stack.pop()

            if not len(stack):
                break

            distance = i - stack[-1] -1
            waters = min(height[i], height[stack[-1]]) - height[top]

            total += distance * waters
            print(i, stack, total)
        stack.append(i)
    return total


print(trap([0,1,0,2,1,0,1,3,2,1,2,1]), 6)
# print(trap([4,2,0,3,2,5]), 9)