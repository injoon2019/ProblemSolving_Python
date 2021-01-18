'''
Problem Solving leetcode swap-nodes-in-pairs
Author: Injun Son
Date: January 18, 2021
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
    def swapPairs(self, head: ListNode) -> ListNode:
        tail = head

        while tail and tail.next:
            tail.val, tail.next.val = tail.next.val, tail.val
            tail = tail.next.next

        return head