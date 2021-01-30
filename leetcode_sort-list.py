'''
Problem Solving leetcode subsets
Author: Injun Son
Date: January 29, 2021
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


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        p = head
        lst = []
        while p:
            lst.append(p.val)
            p = p.next

        lst.sort()

        p = head
        for i in range(len(lst)):
            p.val = lst[i]
            p = p.next
        return head
