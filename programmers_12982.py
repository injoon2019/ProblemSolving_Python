'''
Problem Solving Programmers 12982
Author: Injun Son
Date: November 7, 2020
'''
import math
from itertools import combinations
from itertools import combinations

def solution(d, budget):
    answer = 0
    d = sorted(d)
    for item in d:
        if budget - item >= 0:
            budget -= item
            answer +=1
    return answer

print(solution([1,3,2,5,4], 9))
print(solution([2,2,3,3], 10))