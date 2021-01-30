'''
Problem Solving leetcode search-a-2d-matrix-ii
Author: Injun Son
Date: January 30, 2021
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


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 예외 처리
        if not matrix:
            return False

        # 첫 행위 맨 뒤
        row = 0
        col = len(matrix[0]) - 1

        while row <= len(matrix) - 1 and col >= 0:
            if target == matrix[row][col]:
                return True
            # 타겟이 작으면 왼쪽으로 이동
            elif target < matrix[row][col]:
                col -= 1
            elif target > matrix[row][col]:
                row += 1
        return False


sol = Solution()
print(sol.search(  [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 5))