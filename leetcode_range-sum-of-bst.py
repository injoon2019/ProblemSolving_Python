'''
Problem Solving leetcode range-sum-of-bst
Author: Injun Son
Date: November 13, 2020
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

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        if not root:
            return 0

        return (root.val if low <= root.val <= high else 0) + \
            self.rangeSumBST(root.left, low, high) + \
            self.rangeSumBST(root.right, low, high)