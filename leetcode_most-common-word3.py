'''
Problem Solving leetcode most-common-word
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
    word_dict = collections.defaultdict(int)
    for word in str(paragraph.lower().split()).split(","):
        word = re.sub('[^a-z0-9]', '', word)
        if len(word) > 0:
            word_dict[word] +=1

    max_count, max_word = -1, None
    for key, value in word_dict.items():
        if key not in banned and value > max_count:
            max_count = value
            max_word = key

    return max_word


# print(mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]))
print(mostCommonWord("a, a, a, a, b,b,b,c, c", ["a"]))