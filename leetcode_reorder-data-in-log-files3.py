'''
Problem Solving leetcode reorder-data-in-log-files
Author: Injun Son
Date: October 9, 2020
'''
import sys
from collections import deque
from typing import List

sys.setrecursionlimit(100000)

def reorderLogFiles(logs: List[str]) -> List[str]:
    letters, digits = [], []
    for log in logs:
        if log.split()[1].isdigit():
            digits.append(log)
        else:
            letters.append(log)

    letters.sort(key = lambda x: (x.split()[1:], x.split()[0]))
    return letters + digits

print(reorderLogFiles(["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]))