'''
Problem Solving leetcode Valid-palindrome
Author: Injun Son
Date: January 16, 2021
'''
import sys
from collections import deque
from typing import List

sys.setrecursionlimit(100000)

def isPalindrome(s: str) -> bool:
    str = []
    for char in s.lower():
        if char.isalnum():
            str.append(char)

    return str == str[::-1]

print(isPalindrome("A man, a plan, a canal: Panama"), True)
print(isPalindrome("race a car"), False)