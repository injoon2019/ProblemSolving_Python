'''
Problem Solving Baekjoon 16235
Author: Injun Son
Date: September 22, 2020
'''
import sys
import copy
from itertools import combinations
from collections import deque

N, M, K = map(int, input().split())
graph = []
for _ in range(N):
    tmp = list(map(int, input().split()))
    graph.append(tmp)
