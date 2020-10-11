'''
Problem Solving leetcode two-sum
Author: Injun Son
Date: October 10, 2020
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

# 브루트포스
# def twoSum(nums: List[int], target:int) -> List[int]:
#     for i in range(0, len(nums)-1):
#         for j in range(i+1, len(nums)):
#             if nums[i]+nums[j]==target:
#                 return i, j

# def twoSum(nums: List[int], target:int) -> List[int]:
#     for i, n in enumerate(nums):
#         complement = target - n
#
#         if complement in nums[i+1:]:
#             return nums.index(n), nums[i+1:].index(complement) + (i+1)

# def twoSum(nums: List[int], target:int) -> List[int]:
    # nums_map = {}
    # #키와 값을 바꿔서 딕셔너리로 저장
    # for i, num in enumerate(nums):
    #     nums_map[num] = i
    #
    # #타겟에서 첫 번째 수를 뺀 결과를 키로 조회
    # for i, num in enumerate(nums):
    #     if target - num in nums_map and i != nums_map[target - num]:
    #         return nums.index(num), nums_map[target-num]

def twoSum(nums: List[int], target:int) -> List[int]:
    nums_map = {}
    #하나의 for문으로 통합
    for i, num in enumerate(nums):
        if target - num in nums_map:
            return [nums_map[target - num], i]
        nums_map[num] = i

print(twoSum([2,7,11,15], 9))