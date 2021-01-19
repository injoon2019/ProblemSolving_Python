'''
Problem Solving leetcode valid-parentheses
Author: Injun Son
Date: October 14, 2020
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


def isValid(s:str)-> bool:
    stack = []
    paren_dict = {'(': ')', '{':'}', '[':']'}
    for char in s:
        if char in ['(', '[', '{']:
            stack.append(char)
        else:
            if stack and paren_dict[stack[-1]] == char:
                stack.pop()
                continue
            return False

    return len(stack) == 0
print(isValid("()[]{}"))