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
import re

def isPalindrome(s: str)-> bool:
    s = s.lower()
    #정규식으로 불필요한 문자 필터링
    s = re.sub('[^a-z0-9]', '', s)

    return s==s[::-1]