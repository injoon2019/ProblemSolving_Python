'''
Problem Solving Programmers 42576
Author: Injun Son
Date: Dec 21, 2020
'''
import math
from itertools import combinations
from itertools import combinations
from collections import defaultdict


def solution(participant, completion):
    runner_dict = defaultdict()
    # runner_dict = defaultdict(int)

    for one in participant:
        runner_dict[one] += 1

    for one in completion:
        runner_dict[one] -= 1

    for key, value in runner_dict.items():
        if value == 1:
            return key

print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))
print(solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]))
print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))
