'''
Problem Solving leetcode palindrome-pairs
Author: Injun Son
Date: December 8, 2020
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

class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        def is_palindrome(word):
            return word == word[::-1]

        output = []
        for i, word1 in enumerate(words):
            for j, word2 in enumerate(words):
                if i==j:
                    continue
                if is_palindrome(word1 + word2):
                    output.append([i, j])

        return output