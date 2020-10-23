'''
Problem Solving leetcode letter-combinations-of-a-phone-number
Author: Injun Son
Date: October 22, 2020
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

def letterCombinations(digits: str) -> List[str]:
    num_dict = {"2":['a','b','c'], "3":['d', 'e', 'f'], "4":['g', 'h', 'i'], "5":['j', 'k', 'l'], "6":['m', 'n', 'o'], "7":['p', 'q', 'r', 's'], "8":['t', 'u', 'v'], "9":['w', 'x', 'y', 'z']}
    used_letters = [0]*26
    ans = []

    def back_tracking(cur_index, max_count, cur_str):
        if cur_index == max_count:
            if len(cur_str) > 0:
                ans.append(cur_str)
            return

        for char in num_dict[digits[cur_index]]:
            back_tracking(cur_index+1, max_count, cur_str+char)

    back_tracking(0, len(digits), '')
    return ans

print(letterCombinations("23"))
print(letterCombinations(""))
print(letterCombinations("2"))