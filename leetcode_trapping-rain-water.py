'''
Problem Solving leetcode trapping-rain-water
Author: Injun Son
Date: October 11, 2020
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

#내가 푼 코드
def trap(height: List[int]) -> int:
    height2 = height
    stack = []
    # 스택이 비어있는데 높이가 있는 벽을 만나면 인덱스를 저장하고,
    # 스택 젤 위의 벽의 높이보다 높은 벽을 만나면 계속 팝하며 비워낸다?
    water_sum = 0
    for i in range(len(height2)):
        if stack:
            if height2[i] >= height2[stack[-1]]:
                while len(stack)>=2 and height2[stack[-1]] < height2[i]:
                    stack.pop()

                water_height = min(height2[stack[-1]], height2[i])
                for k in range(stack[-1]+1, i):
                    water_sum += water_height - height2[k]
                    height2[k] = water_height

                if height2[i] > height2[stack[-1]]:
                    stack.pop()
                stack.append(i)

            elif height2[i] < height2[stack[0]]:
                stack.append(i)

        #스택이 비었을 경우
        else:
            #높이가 1이상이면 왼쪽 끝 벽이 생긴거다
            if height2[i]>=1:
                stack.append(i)

        # print(i, stack, water_sum)

    return water_sum

print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))
# print(trap([4,2,0,3,2,5]))