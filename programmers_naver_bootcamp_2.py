'''
Problem Solving Programmers Naver AI bootcamp 2
Author: Injun Son
Date: Dec 22, 2020
'''
import math
from itertools import combinations
from collections import defaultdict
import heapq

def make_count_arr(arr):
    tmp = []
    arr += [-1234567]
    prev_val = -1
    count = 1
    for cur_index in range(len(arr)):
        if arr[cur_index] == prev_val:
            count +=1
        else:
            tmp.append(count)
            prev_val = arr[cur_index]
            count = 1
    return tmp[1:]

def solution(arr):
    answer = 1
    while make_count_arr(arr) != [1]:
        arr = make_count_arr(arr)
        answer +=1
    return answer

print(solution([1, 1, 3, 3, 2, 2, 4, 5, 1, 1, 1, 3, 3, 3]), 6)
print(solution([1,2,3]),3)
print(solution([2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 2, 1, 2]), 5)
print(solution([2]), 1)