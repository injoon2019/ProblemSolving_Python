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
    stack = []
    answer = [0] * len(T)
    for i in range(len(T)):
        while stack and T[i] > T[stack[-1]]:
            answer[stack[-1]] = i - stack[-1]
            stack.pop()
        stack.append(i)
    return answer

print(dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))