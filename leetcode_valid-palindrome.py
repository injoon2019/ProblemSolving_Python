'''
Problem Solving leetcode Valid-palindrome
Author: Injun Son
Date: October 9, 2020
'''
import sys
from collections import deque
sys.setrecursionlimit(100000)

def isPalindrome(s: str)-> bool:
    strs = []
    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    #팰린드롬 여부 판별
    while len(strs) > 1:
        if strs.pop(0) != strs.pop():
            return False

    return True