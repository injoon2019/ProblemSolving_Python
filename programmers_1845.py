'''
Problem Solving Programmers 1845
Author: Injun Son
Date: November 6, 2020
'''
import math
from itertools import combinations

def solution(nums):
    answer = 0
    pocketmon_set = set(nums)

    if len(pocketmon_set) >= len(nums)//2:
        return len(nums)//2
    else:
        return len(pocketmon_set)
    return answer

print(solution([3,1,2,3]))
print(solution([3,3,3,2,2,4]))
print(solution([3,3,3,2,2,2]))