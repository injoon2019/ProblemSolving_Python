'''
Problem Solving Baekjoon 11066
Author: Injun Son
Date: September 18, 2020
'''
import sys
import copy
from itertools import combinations
from collections import deque

T = int(input())
for _ in range(T):
    K = int(input())
    arr = list(map(int, input().split()))
    