'''
Problem Solving Programmers 68644
Author: Injun Son
Date: November 7, 2020
'''
import math
from itertools import combinations
from itertools import combinations

def solution(numbers):
    answer = []
    possible_combs = list(combinations(numbers, 2))
    for comb in possible_combs:
        if comb[0]+comb[1] not in answer:
            answer.append(comb[0]+comb[1])
    return sorted(answer)

print(solution([2,1,3,4,1]))
print(solution([5,0,2,7]))