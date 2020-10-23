'''
Problem Solving leetcode permutations2
Author: Injun Son
Date: October 23, 2020
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

def permute(nums: List[int]) -> List[List[int]]:

    results = []
    prev_elements = []

    def dfs(elements):
        #리프 노드일 때 결과 추가
        if len(elements) == 0:
            #이때 results.append(prev_elements)를 하게되면 결과 값이 추가되는게 아닌 prev_elements에 대한 참조가 추가된다
            results.append(prev_elements[:])

        #순열 생성 재귀 호출
        for e in elements:
            next_elements = elements[:]
            dfs(next_elements)
            prev_elements.pop()

    dfs(nums)
    return results

print(permute([1,2,3]))
print(permute([1]))