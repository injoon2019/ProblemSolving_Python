'''
Problem Solving Programmers Naver AI bootcamp 5
Author: Injun Son
Date: Dec 22, 2020
'''
import math
from itertools import combinations
from collections import defaultdict
import heapq

def get_k(n):
    bin_string = bin(n)[2:]
    count = 0
    for char in bin_string:
        if char == '1':
            count +=1
        return count

def solution(n):
    answer = 0
    k = get_k(n)
    for i in range(1, n):
        tmp = get_k(i)
        if tmp == k:
            answer +=1
    return answer

print(solution(9), 3)