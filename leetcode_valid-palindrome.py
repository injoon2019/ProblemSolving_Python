'''
Problem Solving leetcode Valid-palindrome
Author: Injun Son
Date: October 9, 2020
'''
import sys
from collections import deque
from typing import List

sys.setrecursionlimit(100000)

def reverseString(s: List[str])-> None:
    s.reverse()