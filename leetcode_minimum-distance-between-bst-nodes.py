'''
Problem Solving leetcode minimum-distance-between-bst-nodes
Author: Injun Son
Date: November 15, 2020
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
    prev = -sys.maxsize
    result = sys.maxsize

    # 재귀 구조 중위 순회 비교 결과
    def minDiffInBST(self, root: TreeNode) -> int:
        if root.left:
            self.minDiffInBST(root.left)

            self.result = min(self.result, root.val - self.val)
            self.prev = root.val

            if root.right:
                self.minDiffInBST(root.right)

            return self.result