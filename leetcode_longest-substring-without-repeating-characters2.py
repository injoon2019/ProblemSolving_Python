'''
Problem Solving leetcode ongest-substring-without-repeating-characters2
Author: Injun Son
Date: October 20, 2020
'''
import sys
import collections
from typing import List
from collections import defaultdict
sys.setrecursionlimit(100000)
import re


def lengthOfLongestSubstring(s: str) -> int:
    used = {}
    start = max_length = 0
    for index, char in enumerate(s):
        if char in used and start <= used[char]:
            start = used[char] +1
        else:
            max_length = max(max_length, index-start +1)

        used[char] = index

    return max_length


print(lengthOfLongestSubstring("pwwkew"))