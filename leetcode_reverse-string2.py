'''
Problem Solving leetcode reverse-string2
Author: Injun Son
Date: October 9, 2020
'''
import sys
from collections import deque
from typing import Deque, List

sys.setrecursionlimit(100000)
from collections import deque
import collections
import re

def reverseString(s: List[str]) -> None:
    left, right = 0, len(s)-1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left +=1
        right -=1