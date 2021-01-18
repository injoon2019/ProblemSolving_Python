'''
Problem Solving leetcode palindrome-linked-list
Author: Injun Son
Date: January, 2021
'''
import sys
import collections
import heapq
import functools
import itertools
import re
import math
import bisect
from typing import *


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        tmp = []
        while head != None:
            tmp.append(head.val)
            head = head.next
        return tmp == tmp[::-1]

print(Solution.isPalindrome())