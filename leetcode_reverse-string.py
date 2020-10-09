'''
Problem Solving leetcode reverse-string
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
    s.reverse()