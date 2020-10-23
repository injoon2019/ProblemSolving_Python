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

    def dfs(index, path):
        # 끝까지 탐색하면 백트랙킹
        if len(path) == len(digits):
            result.append(path)
            return

        #입력값 자리수 단위 반복
        for i in range(index, len(digits)):
            # 숫자에 해당하는 모든 문자열 반복
            for j in dic[digits[i]]:
                dfs(i+1, path+j)
    #예외처리
    if not digits:
        return []


    dic = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
    result = []
    dfs(0, "")

    return result

print(letterCombinations("23"))
print(letterCombinations(""))
print(letterCombinations("2"))