'''
Problem Solving leetcode most-common-word
Author: Injun Son
Date: October 9, 2020
'''
import sys
from collections import deque
from typing import List

sys.setrecursionlimit(100000)
import re

def mostCommonWord(paragraph: str, banned: List[str]) ->str:
    words = paragraph.lower()
    words = re.sub('[^a-z]', ' ', words)
    words = words.split()
    word_dic = {}
    for word in words:
        if word not in banned:
            if word in word_dic:
                word_dic[word]+=1
            else:
                word_dic[word] =1

    max_key = max(word_dic, key= word_dic.get)
    return max_key

print(mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]))