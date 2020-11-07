'''
Problem Solving Programmers woowa 5
Author: Injun Son
Date: November 7, 2020
'''
import math
from itertools import combinations
from itertools import combinations
from collections import deque

def solution(penter, pexit, pescape, data):
    answer = penter
    for i in range(0, len(data), len(penter)):
        byte_data = data[i : i+ len(penter)]
        if byte_data in [penter, pexit, pescape]:
            answer += pescape
        answer += byte_data
    answer += pexit
    return answer

print(solution("1100", "0010", "1001", "1101100100101111001111000000"))
print(solution("10", "11", "00", "00011011"))