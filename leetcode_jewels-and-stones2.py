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
    freqs = collections.Counter(S)
    count = 0

    #비교 없이 보석(J) 빈도 수 합산
    for char in J:
        count += freqs[char]

    return count

print(numJewelsInStones("aA", "aAAbbbb"))