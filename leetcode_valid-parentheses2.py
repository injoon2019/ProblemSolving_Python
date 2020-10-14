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
    table = {
        ')' : '(',
        '}' : '{',
        ']' : '['
    }

    #스택 이용 예외 처리 및 일치 여부 판별
    for char in s:
        if char not in table:
            stack.append(char)
        elif not stack or table[char] != stack.pop():
            return False

    return len(stack)==0

print(isValid("()[]{}"))