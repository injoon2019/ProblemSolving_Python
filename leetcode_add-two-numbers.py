'''
Problem Solving leetcode add-two-numbers
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
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        nums1, nums2 = [], []
        while l1 != None:
            nums1.append(str(l1.val))
            l1 = l1.next

        while l2 != None:
            nums2.append(str(l2.val))
            l2 = l2.next

        nums1 = ''.join(nums1[::-1])
        nums2 = ''.join(nums2[::-1])
        ans = int(nums1) + int(nums2)
        ans = [x for x in str(ans)]
        result_head = ListNode()
        tail = result_head
        for i in range(len(ans)-1, -1, -1):
            tail.next = ListNode(int(ans[i]))
            tail = tail.next

        return result_head.next
