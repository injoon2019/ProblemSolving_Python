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
# def trap(height: List[int]) -> int:
#     height2 = height
#     stack = []
#     # 스택이 비어있는데 높이가 있는 벽을 만나면 인덱스를 저장하고,
#     # 스택 젤 위의 벽의 높이보다 높은 벽을 만나면 계속 팝하며 비워낸다?
#     water_sum = 0
#     for i in range(len(height2)):
#         if stack:
#             if height2[i] >= height2[stack[-1]]:
#                 while len(stack)>=2 and height2[stack[-1]] < height2[i]:
#                     stack.pop()
#
#                 water_height = min(height2[stack[-1]], height2[i])
#                 for k in range(stack[-1]+1, i):
#                     water_sum += water_height - height2[k]
#                     height2[k] = water_height
#
#                 if height2[i] > height2[stack[-1]]:
#                     stack.pop()
#                 stack.append(i)
#
#             elif height2[i] < height2[stack[0]]:
#                 stack.append(i)
#
#         #스택이 비었을 경우
#         else:
#             #높이가 1이상이면 왼쪽 끝 벽이 생긴거다
#             if height2[i]>=1:
#                 stack.append(i)
#
#         # print(i, stack, water_sum)
#
#     return water_sum

#책의 투포인터 풀이
# def trap(height: List[int]) -> int:
    # if not height:
    #     return 0
    #
    # volumd = 0
    # left, right = 0, len(height)-1
    # left_max, right_max = height[left], height[right]
    #
    # while left < right:
    #     left_max, right_max = max(height[left], left_max), max(height[right], right_max)
    #
    #     # 더 높은 쪽을 향해 투 포인터 이동
    #     if left_max <= right_max:
    #         pass

# def trap(height: List[int]) -> int:
#     if not height:
#         return 0
#
#     volume = 0
#     left, right = 0, len(height)-1
#     left_max, right_max = height[left], height[right]
#
#     while left < right:
#         left_max, right_max = max(height[left], left_max), max(height[right], right_max)
#
#         #더 높은 쪽을 향해서 투 포인터 이동
#         if left_max <= right_max:
#             volume += left_max - height[left]
#             left +=1
#         else:
#             volume += right_max - height[right]
#             right -=1
#
#     return volume

def trap(height: List[int]) -> int:
    stack = []
    volume = 0

    for i in range(len(height)):
        #현재 높이가 이전 높이보다 높을 때
        while stack and height[i] > height[stack[-1]]:
            #스택에서 꺼낸다
            top = stack.pop()

            if not len(stack):
                break

            #이전과의 차이만큼 물 높이 처리
            distance = i - stack[-1] -1
            waters = min(height[i], height[stack[-1]])- height[top]

            volume += distance*waters

        stack.append(i)

    return volume

print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))
# print(trap([4,2,0,3,2,5]))