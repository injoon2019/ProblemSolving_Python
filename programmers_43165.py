'''
Problem Solving Programmers 43165
Author: Injun Son
Date: Dec 22, 2020
'''
import math
from itertools import combinations
from collections import defaultdict
import heapq

count = 0
def solve(cur_index, cur_sum, target, numbers):
    global count
    if cur_index == len(numbers):
        if cur_sum == target:
            count +=1
        return

    solve(cur_index+1, cur_sum + numbers[cur_index], target, numbers)
    solve(cur_index + 1, cur_sum - numbers[cur_index], target, numbers)

def solution(numbers, target):
    solve(0, 0, target, numbers)
    return count


print(solution([1,1,1,1,1],3))
