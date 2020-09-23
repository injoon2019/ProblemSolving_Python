'''
Problem Solving Baekjoon 6064
Author: Injun Son
Date: September 23, 2020
'''
import sys
import copy
from itertools import combinations
from collections import deque
import math
#https://mygumi.tistory.com/325
# <x:y>는 몇 번째 해를 나타내는지 구하는 프로그램을 작성하라
T = int(input())

def get_year(m, n, x, y):
    while x <= m*n:
        if (x-y)%n == 0:
            return x
        x += m
    return -1

for _ in range(T):
    M, N, x, y = map(int, input().split())
    print(get_year(M, N, x, y))

