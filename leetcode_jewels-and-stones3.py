'''
Problem Solving leetcode jewels-and-stones
Author: Injun Son
Date: October 18, 2020
'''
import sys
import collections
from typing import List
from collections import defaultdict
sys.setrecursionlimit(100000)
import re


def numJewelsInStones(J: str, S: str) -> int:
    return sum(s in J for s in S)

print(numJewelsInStones("aA", "aAAbbbb"))