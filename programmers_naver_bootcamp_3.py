'''
Problem Solving Programmers Naver AI bootcamp 3
Author: Injun Son
Date: Dec 22, 2020
'''
import math
from itertools import combinations
from collections import defaultdict
import heapq

def calculate(origin, dest, total_length):
    dist1 = max(origin, dest) - min(origin, dest)
    dist2 = total_length - dist1
    return min(dist1, dist2)

def solution(N, sequence):
    answer = 0
    for i in range(len(sequence)-1):
        if i ==0:
            answer += calculate(1, sequence[i], N)
        answer += calculate(sequence[i], sequence[i+1], N)

    return answer

print(solution([1,2,3,4,5]), 4)
print(solution([3,5,4,1,2]), 8)
