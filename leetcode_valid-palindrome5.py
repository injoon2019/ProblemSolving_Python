'''
Problem Solving leetcode Valid-palindrome
Author: Injun Son
Date: January 16, 2021
'''
import collections
import sys
from collections import deque
from typing import List

sys.setrecursionlimit(100000)

def isPalindrome(s: str) -> bool:
    # 자료형 데크로 선언
    Deque = collections.deque()

    for char in s:
        if char.isalnum():
            Deque.append(char.lower())

    while len(Deque) > 1:
        if Deque.popleft() != Deque.pop():
            return False

    return True

print(isPalindrome("A man, a plan, a canal: Panama"), True)
print(isPalindrome("race a car"), False)