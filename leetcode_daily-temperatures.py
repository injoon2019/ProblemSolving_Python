'''
Problem Solving leetcode daily-temperatures
Author: Injun Son
Date: October 18, 2020
'''
import sys
from collections import deque
from typing import List

sys.setrecursionlimit(100000)
import re

def dailyTemperatures(T: List[int]) -> List[int]:
    ans = [0]*len(T)
    stack = []
    for i in range(len(T)):
        while stack and  T[i] > T[stack[-1]]:
            ans[stack.pop()] = i - stack[-1]
        stack.append(i)

    return ans


print(dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))