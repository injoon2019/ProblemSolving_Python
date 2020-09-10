'''
Problem Solving Baekjoon 17413_5
Author: Injun Son
Date: September 10, 2020
'''
import sys
from collections import deque

import heapq
import re
sentence_split = input().split("<")
s = ''

for words in sentence_split:
    if ">" in words:
        words2 = words.split(">")
        s+= '<'+words2[0]+'>'+ ' '.join(map(lambda x: x[::-1], words2[1].split()))
    else:
        s += ' '.join(map(lambda x: x[::-1], words.split()))

print(s)