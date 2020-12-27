'''
Problem Solving Programmers 42862
Author: Injun Son
Date: Dec 22, 2020
'''
import math
from itertools import combinations
from itertools import combinations
from collections import defaultdict


def solution(n, lost, reserve):
    reserve_set = set(reserve) - set(lost)
    lost_set = set(lost) - set(reserve)
    for i in reserve_set:
        if i - 1 in lost_set:
            lost_set.remove(i - 1)
        elif i + 1 in lost_set:
            lost_set.remove(i + 1)


    return n - len(lost_set)


print(solution(5, [2, 4], [1, 3, 5]), 5)
print(solution(5, [2, 4], [3]), 4)
print(solution(5, [1, 2, 4, 5], [2, 3, 4]), 3)
