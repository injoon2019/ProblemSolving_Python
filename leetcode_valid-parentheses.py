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
    for c in s:
        if c in ['(', '[', '{']:
            stack.append(c)
        else:
            if len(stack)==0:
                return False
            if c == ')':
                if stack[-1]=='(':
                    stack.pop()
                else:
                    return False
            if c == ']':
                if stack[-1]=='[':
                    stack.pop()
                else:
                    return False
            if c == '}':
                if stack[-1]=='{':
                    stack.pop()
                else:
                    return False

    return len(stack)==0

print(isValid("()[]{}"))