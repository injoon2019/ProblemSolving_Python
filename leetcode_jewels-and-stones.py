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
    freq = collections.defaultdict(int)
    count = 0
    for char in S:
        freq[char] +=1

    for char in J:
        count += freq[char]

    return count

print(numJewelsInStones("aA", "aAAbbbb"))