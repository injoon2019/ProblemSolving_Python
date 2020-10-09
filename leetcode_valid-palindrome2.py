'''
Problem Solving leetcode Valid-palindrom2
Author: Injun Son
Date: October 9, 2020
'''
import sys
from collections import deque
from typing import Deque

sys.setrecursionlimit(100000)
from collections import deque
import collections

def isPalindrome(s: str)-> bool:
    strs: Deque = collections.deque()

    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    while len(strs) > 1:
        if strs.popleft() != strs.pop():
            return False

    return True
