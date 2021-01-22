'''
Problem Solving leetcode letter-combinations-of-a-phone-number3
Author: Injun Son
Date: January 22, 2021
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
    ans = []

    if len(digits) == 0:
        return ans

    def comb_func(cur_index, max_length, cur_string):
        if cur_index == max_length:
            ans.append(cur_string)
            return

        for char in num_dict[digits[cur_index]]:
            comb_func(cur_index+1, max_length, cur_string + char)

    comb_func(0, len(digits), "")
    return ans

print(letterCombinations("23"))
print(letterCombinations(""))
print(letterCombinations("2"))