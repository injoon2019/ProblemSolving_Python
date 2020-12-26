'''
Problem Solving Programmers 42840
Author: Injun Son
Date: Dec 22, 2020
'''
import math
from itertools import combinations
from collections import defaultdict
import heapq

pattern_1 = [1, 2, 3, 4, 5]
pattern_2 = [2, 1, 2, 3, 2, 4, 2, 5]
pattern_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]


def solution(answers):
    index1, index2, index3 = 0, 0, 0
    answer_counts = [0, 0, 0]

    for answer in answers:
        if answer == pattern_1[index1]:
            answer_counts[0] += 1
        if answer == pattern_2[index2]:
            answer_counts[1] += 1
        if answer == pattern_3[index3]:
            answer_counts[2] += 1

        index1 = (index1 + 1) % len(pattern_1)
        index2 = (index2 + 1) % len(pattern_2)
        index3 = (index3 + 1) % len(pattern_3)

    m = max(answer_counts)
    answer = [i + 1 for i, j in enumerate(answer_counts) if j == m]
    return answer


print(solution([1, 2, 3, 4, 5]))
print(solution([1, 3, 2, 4, 2]))
