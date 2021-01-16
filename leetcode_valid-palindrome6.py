'''
Problem Solving leetcode Valid-palindrome
Author: Injun Son
Date: January 16, 2021
'''
import collections
import sys
from collections import deque
from typing import List
import re

sys.setrecursionlimit(100000)

def isPalindrome(s: str) -> bool:
    s = s.lower()
    #정규식으로 문자 필터링
    s = re.sub('[^a-z0-9]', '', s)

    return s == s[::-1]

print(isPalindrome("A man, a plan, a canal: Panama"), True)
print(isPalindrome("race a car"), False)