'''
Problem Solving Programmers Naver AI bootcamp 6
Author: Injun Son
Date: Dec 22, 2020
'''
import math
from itertools import combinations
from collections import defaultdict
import heapq
import sys


def solution(nums):
    answer = 0
    count_arr = [sys.maxsize] * len(nums)
    cur_pos = 0

    def dfs(cur, count):
        count_arr[cur] = count
        right_next_pos = cur + nums[cur]
        left_next_pos = cur - nums[cur]

        if 0 <= right_next_pos < len(nums) and count + 1 < count_arr[right_next_pos]:
            dfs(right_next_pos, count + 1)
        if 0 <= left_next_pos < len(nums) and count + 1 < count_arr[left_next_pos]:
            dfs(left_next_pos, count + 1)

        dfs(0, 0)
        if count_arr[-1] == sys.maxsize:
            return -1
        else:
            return count_arr[-1]
