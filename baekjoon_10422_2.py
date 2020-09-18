'''
Problem Solving Baekjoon 10422_2
Author: Injun Son
Date: September 18, 2020
'''
import sys
import copy
from itertools import combinations
from collections import deque
MOD = 1000000007
t = int(input())
'''
카탈란 상수로 푸는 방법 
'''
import math

def catalan(n):
    return math.factorial(2*n) // (math.factorial(n)*math.factorial(n+1))

for i in range(2, 100, 2):
    print(catalan(i))
# for _ in range(t):
#     n = int(input())
#     print(catalan(n)%MOD)