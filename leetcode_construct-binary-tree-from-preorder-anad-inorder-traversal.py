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

def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
    if inorder:
        # 전위 순회 결과는 중위 순회 분활 인덱스
        index = inorder.index(preorder.pop(0))

        # 중위 순회 결과 분활 정복
        node = TreeNode(inorder[index])
        node.left = self.buildTree(preorder, inorder[0:index])
        node.right = self.buildTree(preorder, inorder[index+1:])

        return node