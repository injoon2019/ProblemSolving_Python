'''
Problem Solving Baekjoon 2805
Author: Injun Son
Date: August 8, 2020
'''
import sys
import math
def cut_left(height):
    wood = 0
    for i in arr:
        if i - height >0:
            wood += (i-height)
    return wood

N, M = map(int, input().split())
arr = list(map(int, input().split()))
max_val = max(arr)
min_val = 1
mid = (max_val + min_val)//2
max_height = 0
while min_val <= max_val:
    #부족하게 자른 상황이므로, 최대 자르는 높이를 낮춰야한다
    if cut_left(mid) < M:
        max_val = mid - 1
        mid = (max_val + min_val) // 2

    #초과하게 자른 상황이므로 자르는 높이를 높여야한다.
    elif cut_left(mid) >= M:
        if max_height < mid:
            max_height = mid
        min_val = mid + 1
        mid = (max_val + min_val) // 2

print(max_height)