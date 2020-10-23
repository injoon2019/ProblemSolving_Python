'''
Problem Solving leetcode combination-sum
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


def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
    result = []

    def dfs(csum, index, path):
        # 종료 조건
        if csum < 0:
            return
        if csum ==0:
            result.append(path)
            return

        # 자신부터 하위 원소까지 나열 재귀 호출
        for i in range(index, len(candidates)):
            dfs(csum - candidates[i], i, path + [candidates[i]])

    dfs(target, 0, [])
    return result

print(combinationSum([2,3,6,7], 7))