'''
Problem Solving leetcode remove-duplicate-letters
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


def removeDuplicateLetters(s: str) -> str:
    counter, stack = collections.Counter(s), []

    for char in s:
        counter[char] -=1
        if char in stack:
            continue

        #뒤에 붙일 문자가 남아 있다면 스택에서 제거
        while stack and char < stack[-1] and counter[stack[-1]] > 0:
            stack.pop()
        stack.append(char)

    return ''.join(stack)

print(removeDuplicateLetters("cbacdcbc"))