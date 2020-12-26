'''
Problem Solving Programmers Naver AI bootcamp 1
Author: Injun Son
Date: Dec 22, 2020
'''
import math
from itertools import combinations
from collections import defaultdict
import heapq

def solution(s):
    answer = 0
    count = [0] * 26
    odd_count = 0
    for char in s:
        count[ord(char)-ord('a')] +=1

    for i in range(len(count)):
        if count[i] % 2 == 1:
            odd_count +=1
    return odd_count

print(solution("aabbbccd"), 2)
print(solution("abebeaedeac"), 3)