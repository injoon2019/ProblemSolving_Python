'''
Problem Solving leetcode ongest-substring-without-repeating-characters3
Author: Injun Son
Date: January 21, 2021
'''
import sys
import collections
from typing import List
from collections import defaultdict
sys.setrecursionlimit(100000)
import re


def lengthOfLongestSubstring(s: str) -> int:
    used = {}
    max_length = start = 0
    for index, char in enumerate(s):
        if char in used and start <= used[char]:
            start = used[char] + 1
        else:
            max_length = max(max_length, index - start + 1)

        used[char] = index

    return max_length


# print(lengthOfLongestSubstring("pwwkew"))
# print(lengthOfLongestSubstring("abcabcbb"))
print(lengthOfLongestSubstring(" "), 1)
print(lengthOfLongestSubstring("aabaab!bb"), 3)