'''
Problem Solving leetcode palindrome-linked-list
Author: Injun Son
Date: October 12, 2020
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

def isPalindrome(head: ListNode) -> bool:
    tmp = []

    while head != None and head.next != None:
        tmp.append(head.val)
        head = head.next
        if head == None:
            break

    if head != None:
        tmp.append(head.val)
    return tmp == tmp[::-1]

print(isPalindrome())