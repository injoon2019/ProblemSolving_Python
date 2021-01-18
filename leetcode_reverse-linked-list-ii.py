'''
Problem Solving leetcode reverse-linked-list-ii
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
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head or m==n:
            return head

        root = start = ListNode(None)
        root.next= head
        # start, end 지정
        for _ in range(m-1):
            start = start.next
        end = start.next

        # 반복하면서 노드 차례대로 뒤집기
        for _ in range(n - m):
            tmp = start.next
            start.next = end.next
            end.next = end.next.next
            start.next.next = tmp

        return root.next