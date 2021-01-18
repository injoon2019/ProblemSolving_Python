'''
Problem Solving leetcode merge-two-sorted-lists
Author: Injun Son
Date: October 14, 2020
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

def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    head = ListNode()
    tail = head
    while l1 and l2:
        if l1.val <= l2.val:
            tail.next = ListNode(l1.val)
            tail = tail.next
            l1 = l1.next
        else:
            tail.next = ListNode(l2.val)
            tail = tail.next
            l2 = l2.next

    while l1:
        tail.next = ListNode(l1.val)
        l1 = l1.next
        tail = tail.next

    while l2:
        tail.next = ListNode(l2.val)
        l2 = l2.next
        tail = tail.next

    return head.next
