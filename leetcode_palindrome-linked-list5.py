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
        q: Deque = []

        if not head:
            return True

        node = head
        # 리스트 변환
        while node is not None:
            q.append(node.val)
            node = node.next

        # 팰린드롬 판별
        while len(q) > 1:
            if q.popleft() != q.pop():
                return False
        return True

print(Solution.isPalindrome())