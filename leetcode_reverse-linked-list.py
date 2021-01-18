'''
Problem Solving leetcode reverse-linked-list
Author: Injun Son
Date: January 18, 2021
'''
import sys
from collections import deque
from typing import Deque, List

sys.setrecursionlimit(100000)
from collections import deque
import collections
import re

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        tmp = []
        while head != None:
            tmp.append(head.val)
            head = head.next

        return_head = tail = ListNode()
        for num in tmp[::-1]:
            tail.next = ListNode(num)
            tail = tail.next

        return return_head.next