'''
Problem Solving leetcode convert-sorted-array-to-binary-search-tree
Author: Injun Son
Date: November 11, 2020
'''
import sys
import collections
import heapq
import functools
import itertools
import re
import math
import bisect
from collections import deque
from typing import *

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None

        mid = len(nums) // 2

        # 분할 정복으로 이진 검색 결과 트리 구성
        node  = TreeNode(nums[mid])
        node.left = self.sortedArrayToBST(nums[:mid])
        node.right = self.sortedArrayToBST(nums[mid+1: ])

        return node