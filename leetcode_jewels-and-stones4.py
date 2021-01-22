'''
Problem Solving leetcode jewels-and-stones4
Author: Injun Son
Date: January 21, 2021
'''
import sys
import collections
from typing import List
from collections import defaultdict
sys.setrecursionlimit(100000)
import re


def numJewelsInStones(jewels: str, stones: str) -> int:
    stone_dict = collections.defaultdict(int)
    for stone in list(stones):
        if stone in list(jewels):
            stone_dict[stone] += 1

    return sum(stone_dict.values())



print(numJewelsInStones("aA", "aAAbbbb"))