'''
Problem Solving leetcode most-common-word2
Author: Injun Son
Date: October 9, 2020
'''
import collections
import sys
from collections import deque
from typing import List

sys.setrecursionlimit(100000)
import re

def mostCommonWord(paragraph: str, banned: List[str]) ->str:
    words = [word for word in re.sub(r'[^\w]', ' ', paragraph)
        .lower().split()
                if word not in banned]

    counts = collections.Counter(words)
    return counts.most_common(1)[0][0]

print(mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]))