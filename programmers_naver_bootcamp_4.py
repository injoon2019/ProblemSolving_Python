'''
Problem Solving Programmers Naver AI bootcamp 4
Author: Injun Son
Date: Dec 22, 2020
'''
import math
from itertools import combinations
from collections import defaultdict
import heapq

def solution(n):
    arr = [0] * n
    N = n -1
    a, c, b = 2, 1, 0
    for i in range(len(arr)):
        if i != 0 and i%4 == 0:
            b = a * (a+1) * (a+2)
            arr[i] = b
            a +=1
            b = 0
        else:
            arr[i] = c * (c+1)
            c +=1
    return arr[N]

print(solution(1), 2)
print(solution(2), 6)
print(solution(4), 20)
print(solution(9), 60)
