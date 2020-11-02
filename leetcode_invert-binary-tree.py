'''
Problem Solving leetcode invert-binary-tree
Author: Injun Son
Date: November 2, 2020
'''
import heapq
import sys
import collections
from typing import List
from collections import defaultdict
sys.setrecursionlimit(100000)
import re
from collections import deque
        
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
            return root
        return None